$(document).ready(function () {
    $('#expand_btn').click(function () {
        var $hiddenItems = $('.brand-grid.hidden');
        var $changeText = $('#change_text');
        var isExpanded = $changeText.text() === $changeText.data('expanded');

        if (isExpanded) {
            // Collapse all: Set display to 'none' for hidden elements and update the text to 'Expand All'
            $hiddenItems.css('display', 'none');
            $changeText.text($changeText.data('collapsed'));
        } else {
            // Expand all: Set display to 'block' for hidden elements and update the text to 'Collapse All'
            $hiddenItems.css('display', 'block');
            $changeText.text($changeText.data('expanded'));
        }
    });
});

