from django import forms

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
    
    