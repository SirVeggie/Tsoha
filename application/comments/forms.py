from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class CommentForm(FlaskForm):
    title = StringField("Title" , [validators.Regexp('\w+'
                                    , message='- Title must not be empty -')
                                , validators.Length(max=50
                                    , message='- Title is too long -')])

                                    
    content = TextAreaField("content", [validators.Regexp('\w+'
                                        , message='- Content must not be empty -')
                                    , validators.Length(max=500
                                        , message='- Content is too long -')])

    class Meta:
        csrf = False