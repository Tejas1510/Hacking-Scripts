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
                let x = s.charCodeAt(i) - 65;
                ans += String.fromCharCode((x + rot) % 26 + 65);
            }
            else if(s.charCodeAt(i) >= 97 && s.charCodeAt(i) <= 122) {
                let x = s.charCodeAt(i) - 97;
                ans += String.fromCharCode((x + rot) % 26 + 97);
            }
            else {
                ans += s.charAt(i);
            }
        }
        $('#strout').val(ans);
    });
});