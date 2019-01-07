// Dropdowns
$(".ui.dropdown select")
  .not("[name*=__prefix__]")
  .each(function() {
    $(this).dropdown({
      fullTextSearch: true,
      forceSelection: false // https://github.com/Semantic-Org/Semantic-UI/issues/4506
    });
  });

// Autocompletes
$(".admin-autocomplete")
  .not("[name*=__prefix__]")
  .each(function() {
    var url = $(this).data("ajax-url") + "?term={query}";
    $(this).dropdown({
      apiSettings: { url: url, cache: false },
      fullTextSearch: true,
      forceSelection: false,
      saveRemoteData: false
    });
  });

// Checkboxes
$(".ui.checkbox")
  .not("[name*=__prefix__]")
  .each(function() {
    $(this).checkbox();
  });

// Datetime
$(".ui.calendar.datetime")
  .not("[name*=__prefix__]")
  .each(function() {
    $(this).calendar();
  });

// Date
$(".ui.calendar.date")
  .not("[name*=__prefix__]")
  .each(function() {
    $(this).calendar({
      type: "date",
      formatter: {
        date: function(date, settings) {
          if (!date) return "";
          var year = date.getFullYear();
          var month = ("0" + (date.getMonth() + 1)).slice(-2);
          var day = ("0" + date.getDate()).slice(-2);
          return year + "-" + month + "-" + day;
        }
      }
    });
  });

// Time
$(".ui.calendar.time")
  .not("[name*=__prefix__]")
  .each(function() {
    $(this).calendar({ type: "time" });
  });
