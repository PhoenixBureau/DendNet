
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
  if (_.isNull(tag)) {
    return '';
  }
  return tag;
}

function note_own_url(url) {
  $.cookie("own_url", url, {
    expires: 35,
    path: '/',
  })
}

function get_own_url() {
  var url = $.cookie("own_url");
  if (_.isNull(url)) {
    return '';
  }
  return url;
}

