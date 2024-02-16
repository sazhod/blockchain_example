from wtforms import (SubmitField, HiddenField,
                     Form, BooleanField)


class AuthForm(Form):
    fld1 = HiddenField("Field 1", id='test', render_kw={'value': 'test'})
    # fld2 = SubmitField("Field 2", render_kw={'onclick': 'connectWalletwithMetaMask()'})
    fld3 = BooleanField("Field 3", render_kw={'type': 'button', 'onclick': 'connectWalletwithMetaMask()', 'value': 'test'})
