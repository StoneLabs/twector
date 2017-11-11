$(function () {
    $('#options .input input').on("keyup", function () {
        validateImput($(this))
    });
    $('#submit-button').on('click', function () {
        var errors = false;
        // check if error occurs
        $('#options .input input').each(function () {
            if (!validateImput($(this))) {
                errors = true;
                $(this).closest('.input').addClass('error');
            }
        });

        if (errors)
            return;

        loadIndex($('#twector-first-name'), $('#twector-second-name'));
    });
    function validateImput(element) {
        var val = element.val();

        // adding an @ if not exists
        if (val.length > 0 && val[0] !== '@')
            element.val('@' + val);
        // removes the @ for the validation pattern
        else if (val[0] === '@')
            val = val.substr(1);

        // validate twitter name
        if (val.match('^[A-Za-z0-9_]{1,32}$') || val.length < 1)
            element.closest('.input').removeClass('error');
        else
            element.closest('.input').addClass('error');

        return val.match('^[A-Za-z0-9_]{1,32}$') && val.length > 0;
    }
    function loadIndex(firstName, secondName) {
        // loads the site context
    }
});