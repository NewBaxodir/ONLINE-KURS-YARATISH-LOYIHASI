// typed
let options = {
  strings: ["Biz veb-dasturlash, o'yin yaratish va dasturiy ta'minot ishlab chiqishni o'rgatamiz.", " Kurslarni oling, muammolarni hal qiling, yangiliklarni ko'ring va dasturlashning haqiqiy ustasiga aylaning!"],
  typeSpeed: 60,
  startDelay: 200,
  backSpeed: 60,
  backDelay: 200,
  loop: true,
  loopCount: Infinity
};
let typed = new Typed(".element", options);

// vanila 
VanillaTilt.init(document.querySelectorAll(".card"), {
  max: 25,
  speed: 400,
  glare: true,
  "max-glare": 1,

});


// copy link
// const copyToClipboard = str => {
//   const el = document.createElement('textarea');
//   el.value = str;
//   document.body.appendChild(el);
//   el.select();
//   document.execCommand('copy');
//   document.body.removeChild(el);
// };

// const url = 'http://t.me/yagafarovd';

// document.getElementById('myItem').addEventListener('click', function () {
//   let myUrl = url;
//   copyToClipboard(myUrl);
//   comsole.log(myUrl + ' havola nusxalandi!')
// });

// function myFunction() {
//   let x = document.getElementById("snackbar");
//   x.className = "show";
//   setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
// }

// chat
let $messages = $('.messages-content'),
  d, h, m,
  i = 0;


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate() {
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function () {
    fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function () {
  insertMessage();
});

$(window).on('keydown', function (e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})
