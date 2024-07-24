from django import forms
from django.core.mail import EmailMessage
import os

from .models import Question

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=50)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)
    
    """
    argsは、引数の個数をタプルとして可変で入れられる
    kwargsは、引数の個数を辞書型として可変で入れられる
    
    また、辞書としてデータを受けるために、kwargsを使っている
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        """
        dictionary型では基本的に
        d = {a:10,b:20}のように指定するがこの値を取り出すときは
        d[a]のように[]でキーを指定して取り出す
        """
    
    
        """
        self.fieldsで各インスタンス（データ）ごとのフィールドにアクセス
        その中でフィールド名を辞書のキーとして参照し、そこにbootstrapの関数？メソッドを追尾させている
        
        """
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'
    
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']
        
        subject = 'お問い合わせ{}',format(title)
        message = '送信者名:{0}\n メールアドレス:{1}\n メッセージ:\n{2}'.format(name,email,message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
            ]
        
        cc_list = [
            email
        ]
        
        message = EmailMessage(subject=subject,body=message, from_email=from_email,to=to_list,cc=cc_list)
        message.send()
        
class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','content','photo',]
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class']='form-control'