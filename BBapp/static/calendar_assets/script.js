
!function() {
  const button = document.getElementById("theButton")
  window.Calendar = Calendar;

button.onclick=(function () {
  $.ajax({
    type: "POST",
    url: "/receiver",
    success: function (response) {
      let x = JSON.stringify(response)
      console.log(x);
    },
  });
});

  var today = moment();

  function Calendar(selector, events) {
    this.el = document.querySelector(selector);
    this.events = events;
    this.current = moment().date(1);
    this.draw();
    var current = document.querySelector('.today');
    if(current) {
      var self = this;
      window.setTimeout(function() {
        self.openDayDetails(current);
      }, 300);
    }
  }

  Calendar.prototype.draw = function() {
    this.drawHeader();
    this.drawMonth();
  }

  Calendar.prototype.drawHeader = function() {
    var self = this;
    if(!this.header) {
      //Create the header elements
      this.header = createElement('div', 'header');
      this.header.className = 'header';

      this.title = createElement('h1');

      //Left and right arrow, execute next month/prev month function when clicked
      var rightArrow = createElement('div', 'right');
      rightArrow.addEventListener('click', function() { self.nextMonth();});

      var leftArrow = createElement('div', 'left');
      leftArrow.addEventListener('click', function() { self.prevMonth();});

      //Append the Elements
      this.header.appendChild(this.title); 
      this.header.appendChild(rightArrow);
      this.header.appendChild(leftArrow);
      this.el.appendChild(this.header);
    }

    this.title.innerHTML = this.current.format('MMMM YYYY');
  }


  Calendar.prototype.drawMonth = function() {
    var self = this;
    
    this.events.forEach(function(ev) {
     ev.date = moment(ev.date);
    });
    
    //If a month exists, use animation to swap old month out
    if(this.month) {
      this.oldMonth = this.month;
      this.oldMonth.className = 'month out ' + (self.next ? 'next' : 'prev');
      this.oldMonth.addEventListener('webkitAnimationEnd', function() {
        self.oldMonth.parentNode.removeChild(self.oldMonth);
        self.month = createElement('div', 'month');
        self.AddDaysFromPriorMonth();
        self.AddDaysFromCurrentMonth();
        self.AddDaysFromNextMonth();
        self.el.appendChild(self.month);
        window.setTimeout(function() {
          self.month.className = 'month in ' + (self.next ? 'next' : 'prev');
        }, 30);
      });
    } else {
        this.month = createElement('div', 'month');
        this.el.appendChild(this.month);
        this.AddDaysFromPriorMonth();
        this.AddDaysFromCurrentMonth();
        this.AddDaysFromNextMonth();
        this.month.className = 'month new';
    }
  }

  Calendar.prototype.nextMonth = function() {
    this.current.add('months', 1);
    this.next = true;
    this.draw();
  }

  Calendar.prototype.prevMonth = function() {
    this.current.subtract('months', 1);
    this.next = false;
    this.draw();
  }

  Calendar.prototype.AddDaysFromPriorMonth = function() {
    var clone = this.current.clone();
    var dayOfWeek = clone.day();

    if(!dayOfWeek) { return; }

    clone.subtract('days', dayOfWeek+1);

    for(var i = dayOfWeek; i > 0 ; i--) {
      this.drawDay(clone.add('days', 1));
    }
  }

  Calendar.prototype.AddDaysFromNextMonth = function() {
    var clone = this.current.clone().add('months', 1).subtract('days', 1);
    var dayOfWeek = clone.day();

    if(dayOfWeek === 6) { return; }

    for(var i = dayOfWeek; i < 6 ; i++) {
      this.drawDay(clone.add('days', 1));
    }
  }

  Calendar.prototype.AddDaysFromCurrentMonth = function() {
    var clone = this.current.clone();

    while(clone.month() === this.current.month()) {
      this.drawDay(clone);
      clone.add('days', 1);
    }
  }

  Calendar.prototype.getWeek = function(day) {
    if(!this.week || day.day() === 0) {
      this.week = createElement('div', 'week');
      this.month.appendChild(this.week);
    }
  }

  Calendar.prototype.drawDay = function(day) {
    var self = this;
    this.getWeek(day);
    var outer = createElement('div', this.getDayName(day));
    outer.addEventListener('click', function() {
      self.openDayDetails(this);
    });

    var number = createElement('div', 'day-number', day.format('DD'));
    var name = createElement('div', 'day-name', day.format('ddd'));


    //Events in compact form
    var events = createElement('div', 'day-events');
    this.drawEvents(day, events);

    outer.appendChild(number);
    outer.appendChild(name);
    outer.appendChild(events);
    this.week.appendChild(outer);
  }

  Calendar.prototype.drawEvents = function(day, element) {
    if(day.month() === this.current.month()) {
      var todaysEvents = this.events.reduce(function(memo, ev) {
        if(ev.date.isSame(day, 'day')) {
          memo.push(ev);
        }
        return memo;
      }, []);

      todaysEvents.forEach(function(ev) {
        var evSpan = createElement('span', ev.color);
        element.appendChild(evSpan);
      });
    }
  }

  Calendar.prototype.getDayName = function(day) {
    classes = ['day'];
    if(day.month() !== this.current.month()) {
      classes.push('other');
    } else if (today.isSame(day, 'day')) {
      classes.push('today');
    }
    return classes.join(' ');
  }

  //Details upon clicking a day
  Calendar.prototype.openDayDetails = function(el) {
    var details;
    var dayNumber = +el.querySelectorAll('.day-number')[0].innerText || +el.querySelectorAll('.day-number')[0].textContent;
    var day = this.current.clone().date(dayNumber);

    var currentlyOpenedDay = document.querySelector('.details');

    //Check to see if there is an open details box on the current row
    if(currentlyOpenedDay && currentlyOpenedDay.parentNode === el.parentNode) {
      details = currentlyOpenedDay;
    } else {

      //If another day is currently open, close that day's details
      if(currentlyOpenedDay) {
          currentlyOpenedDay.parentNode.removeChild(currentlyOpenedDay);
        currentlyOpenedDay.className = 'details out';
      }

      //Create the Details Container
      details = createElement('div', 'details in');

      el.parentNode.appendChild(details);
    }

    var todaysEvents = this.events.reduce(function(memo, ev) {
      if(ev.date.isSame(day, 'day')) {
        memo.push(ev);
      }
      return memo;
    }, []);

    this.renderEvents(todaysEvents, details);

  }

  Calendar.prototype.renderEvents = function(events, ele) {
    //Remove any events in the current details element
    var currentEventWrapper = ele.querySelector('.events');
    var wrapper = createElement('div', 'events in' + (currentEventWrapper ? ' new' : ''));

    events.forEach(function(ev) {
      var div = createElement('div', 'event');
      var square = createElement('div', 'event-category ' + ev.color);
      var time = createElement('div', '', ev.date);
      var span = createElement('span', '', ev.eventName);

      div.appendChild(square);
      div.appendChild(span);
      div.appendChild(time);
      wrapper.appendChild(div);
    });

    if(events.length == 0) {
      //If no events are on that day, write a placeholder wrapper displaying no events
      var div = createElement('div', 'event empty');
      var span = createElement('span', '', 'No Events Today');
      div.appendChild(span);
      wrapper.appendChild(div);
    }

    //When drawing events, remove all wrappers from currently drawn event
    if(currentEventWrapper) {
      currentEventWrapper.className = 'events out';
        currentEventWrapper.parentNode.removeChild(currentEventWrapper);
        ele.appendChild(wrapper);
        currentEventWrapper.parentNode.removeChild(currentEventWrapper);
        ele.appendChild(wrapper);
        currentEventWrapper.parentNode.removeChild(currentEventWrapper);
        ele.appendChild(wrapper);
        currentEventWrapper.parentNode.removeChild(currentEventWrapper);
        ele.appendChild(wrapper);
    } else {
      ele.appendChild(wrapper);
    }
  }


  function createElement(tagName, className, innerText) {
    var ele = document.createElement(tagName);
    if(className) {
      ele.className = className;
    }
    if(innerText) {
      ele.innderText = ele.textContent = innerText;
    }
    return ele;
  }
}();

!function() {
  var data = [

    { eventName: 'Test1', calendar: 'Other', color: 'orange' , date: new Date(2023, 11, 5, 19, 20, 0)},
    { eventName: 'Test2', calendar: 'Other', color: 'green' , date: new Date(2023, 11, 2, 19, 20, 0) },
    { eventName: 'Test3', calendar: 'Other', color: 'green' , date: new Date(2023, 11, 3, 19, 20, 0) },
    { eventName: 'Test4', calendar: 'Other', color: 'green' , date: new Date(2023, 11, 1, 19, 20, 0) }
  ];


  var drawCalendar = new Calendar('#calendar', data);

}();