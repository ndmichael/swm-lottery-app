from django import forms
from django.contrib.auth.models import User
from .models import Drawing, Pick

# from crispy_forms.bootstrap import InlineCheckboxes


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": "7"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control-lg rounded-9 mb-3"}
        )
        self.fields["subject"].widget.attrs.update(
            {"class": "form-control-lg rounded-9 mb-3"}
        )
        self.fields["message"].widget.attrs.update(
            {"class": "form-control-lg rounded-9 mb-3"}
        )


class PickForm(forms.Form):
    numbers = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
        (21, 21),
        (22, 22),
        (23, 23),
        (24, 24),
        (25, 25),
        (26, 26),
        (27, 27),
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31),
        (32, 32),
        (33, 33),
        (34, 34),
        (35, 15),
        (36, 36),
        (37, 37),
        (38, 38),
        (39, 39),
        (40, 40),
        (41, 41),
        (42, 42),
        (43, 43),
        (44, 44),
        (45, 45),
        (46, 46),
        (47, 47),
        (48, 48),
        (49, 49),
        (50, 50),
        (51, 51),
        (52, 52),
        (53, 53),
        (54, 54),
        (55, 55),
        (56, 56),
        (57, 57),
        (58, 58),
        (59, 59),
    )

    sp_numbers = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
    )
    ball_numbers = forms.ChoiceField(
        choices=numbers,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "draw test", "required": True}
        ),
    )
    special_number = forms.ChoiceField(
        choices=sp_numbers,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "draw test2", "required": True}
        ),
    )
