$(document).ready(function () {
    let rot;
    $('select').on('change', function () {
        rot = parseInt($(this).val());
        $('#strin, #strout').val('');
    }).trigger('change');
    $('#strin').keyup(function () {
        let s = $(this).val(), ans = '';
        for (let i in s) {
            if (s.charCodeAt(i) >= 65 && s.charCodeAt(i) <= 90) {
                let x = s.charCodeAt(i);
                x -= rot;
                if (x < 65) {
                    x = 65 - x;
                    x = 91 - x;
                    ans += String.fromCharCode(x);
                }
                else {
                    ans += String.fromCharCode(x);
                }
            }
            else if (s.charCodeAt(i) >= 97 && s.charCodeAt(i) <= 122) {
                let x = s.charCodeAt(i);
                x -= rot;
                if (x < 97) {
                    x = 97 - x;
                    x = 123 - x;
                    ans += String.fromCharCode(x);
                }
                else {
                    ans += String.fromCharCode(x);
                }
            }
            else {
                ans += s.charAt(i);
            }
        }
        $('#strout').val(ans);
    });
});
