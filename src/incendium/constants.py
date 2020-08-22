# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Constants module."""

# Email settings.
SMTP = 'mail.mycompany.com:25'
SENDER = 'no-reply@mycompany.com'

# Email templates.
ERROR_REPORT = """<html>
    <body>
        <font face='verdana'>
            <b>Error Report.</b><br /><br />
            <b>Error Message</b><br />
            <p>%s</p><br /><br />
            <b>Error Details</b>
            <p>%s</p><br /><br />
            <b>System Details</b><br /><br />
            *** Please do not reply to this email address.
        </font>
    </body>
</html>"""

# Language settings.
DEFAULT_LANGUAGE = 'en_US'

# Button's text property.
CANCEL_TEXT = 'Cancel'
NO_TEXT = 'No'
OK_TEXT = 'OK'
YES_TEXT = 'Yes'

# Strings.
CANNOT_DELETE_ELEMENT = 'This item cannot be deleted.'
CANNOT_EDIT_ELEMENT = 'This item cannot be edited.'
CONFIRM = 'Confirm'
EDIT_ERROR = 'The following errors occurred:'
EDIT_SUCCESS = 'Your changes were saved successfully.'
EDIT_SUCCESS_WITH_ERRORS = 'Your changes were saved with the following errors:'
EMPTY_STRING = ''
ERROR_WINDOW_TITLE = 'Error'
FORM_ERROR = 'Please provide information in the following fields:'
INFO_WINDOW_TITLE = 'Information'
NEW_LINE = '\n'
NEW_TABBED_LINE = '\n    - '
PROCEED_WITH_ROW_DELETION = ('Are you sure you would like to delete the '
                             'selected row?')
PROCEED_WITH_ROWS_DELETION = 'Are you sure you would like to delete all rows?'
PROCEED_WITH_SAVING_CHANGES = 'Are you sure you would like to proceed?'
PROCEED_WITHOUT_SAVING_CHANGES = ('Would you like to proceed without saving '
                                  'your changes?')
SUCCESS_WINDOW_TITLE = 'Success'
TABBED_LINE = '    - '
UNEXPECTED_ERROR = 'An unexpected error occurred in %s. \n%s'
UNEXPECTED_ERROR_CAUSED_BY = ('An unexpected error occurred in %s. '
                              '\n%s\nCaused by: %s')
WARNING_WINDOW_TITLE = 'Warning'
