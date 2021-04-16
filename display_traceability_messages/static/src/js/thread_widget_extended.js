odoo.define('display_traceability_messages.thread_widget_extended', function (require) {
    "use strict";

    var thread_widget = require('mail.widget.Thread');
    var mailUtils = require('mail.utils');   

    var UpdateTimestamps = thread_widget.include({
        _updateTimestamps: function(){
            var isAtBottom = this.isAtBottom();
            this.$('.o_mail_timestamp').each(function () {
                var date = $(this).data('date'); 
                $(this).html(String(date.format('L')) + ' ' + date.format('HH:mm:ss') + ' (' + String(mailUtils.timeFromNow(date)) + ')');
            });
            if (isAtBottom && !this.isAtBottom()) {
                this.scrollToBottom();
            }
        }
    });
    return UpdateTimestamps;
});
