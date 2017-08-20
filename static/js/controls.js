
function engage_action () {
    $.get(engage_url, function(data) {
        if (data.result) {
            window.location.href = iframe_url;
        }
    });
}

function forward_action () {
    $('#forward_dialog').reveal();
}

function reject_action () {
    $('#reject_dialog').reveal();
}

function reject_it () {
    var reason = $('#id_reject_reason').val().substring(0, 256);
    $.post(reject_url, {'reason': reason}, function(data) {
        if (data.result) {
            window.location.href = base_url_here() + 'rejected/';
        }
    });
    close_reject_dialog();
}

function size_iframe () {
    var window_height = $(window).height();
    var controls_height = $(".container").height();
    var iframe_height = window_height - controls_height - 4;
    $("iframe").height(iframe_height);
}

function setup_button(selector, icon, action) {
    $(selector)
      .button({icons:{secondary:icon},})
      .click(action);
}

function close_forward_dialog() {
  $('#forward_dialog').trigger('reveal:close');
}

function close_reject_dialog() {
  $('#reject_dialog').trigger('reveal:close');
}

function close_explain_dialog() {
  $('#explain_dialog').trigger('reveal:close');
}

function note_own_tag(tag) {
  $.cookie("own_tag", tag, {
    expires: 35,
    path: '/',
  })
}

function get_own_tag() {
  var tag = $.cookie("own_tag");
  return _.isNull(tag) ? '' : tag;
}

function note_own_url(url) {
  $.cookie("own_url", url, {
    expires: 35,
    path: '/',
  })
}

function get_own_url() {
  var url = $.cookie("own_url");
  return _.isNull(url) ? '' : url;
}

function base_url_here() {
  return (window.location.protocol + '//' +
          window.location.host + '/');
}
