$(function () {
    $('#options .input input').on("keyup", function ( e ) {
        if(e.which === 13)
            loadButtonClick();
        else
            validateImput($(this))
    });
    $('#submit-button').on('click', function () {
        loadButtonClick()
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
        if ((val.match('^[A-Za-z0-9_]{1,32}$') || val.length < 1) &&
            $('#twector-first-name').val() !== $('#twector-second-name'))
            element.closest('.input').removeClass('error');
        else
            element.closest('.input').addClass('error');

        return val.match('^[A-Za-z0-9_]{1,32}$') && val.length > 0 &&
            $('#twector-first-name').val() !== $('#twector-second-name').val();
    }
    function loadButtonClick() {
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
    }
    function loadIndex(firstName, secondName) {
        // loads the site context
        console.log('loaded');
        $('#options').addClass('loading');
    }
});

// window load event
$(window).on('load', function () {
    console.log('window.load');
    // focus the first input on load
    $('#twector-first-name').focus();
});