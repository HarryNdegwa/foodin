from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, Field, Submit
from django import forms

from .models import Reservation, Contact, Comment


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field("name", css_class="r_field field"),
                Field("email", css_class="r_field field"),
                style="display:flex; flex-wrap:wrap; justify-content:space-between;",
            ),
            Div(
                Field("person", css_class="r_field field"),
                Field("date", css_class="r_field field"),
                style="display:flex; flex-wrap:wrap; justify-content:space-between;",
            ),
            Field("message", css_class="r_field", id="message-field"),
            Submit("submit", "Book Now", css_id="r-btn"),
        )

        super(ReserveForm, self).__init__(*args, **kwargs)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("email"),
            Field("enquiry", id="enq-field"),
            Submit("submit", "Send", css_id="c-btn"),
        )

        super(ContactForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("comment", id="com-field"), Submit("submit", "Post", css_id="com-btn")
        )

        super(CommentForm, self).__init__(*args, **kwargs)

