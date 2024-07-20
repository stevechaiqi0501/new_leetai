from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
import logging
from .models import Question
from accounts.models import CustomUser
"""
ログを記録するときに、どこのモジュールから受け取ったか出力するための__name__
loggerでオブジェクトを取得、中身はloggingクラスのgetLoggerメソッド、そしてどこのモジュールから受け取ったか出力するための__name__
"""    
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = 'index.html'
    
class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    #このクラスの処理に問題がなかったらどこのテンプレートに着地するのか
    success_url = reverse_lazy('Leetai_app:inquiry')
    
    """
    FormViewで定義されているメソッド
    フォームのバリデーション(入力されたレコードが入力条件を満たしているか)の結果、問題がなかったら実行される処理
    
    formの中にはフォームオブジェクトが入っている
    """
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました')
        #ロガー版print
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.send_email()
        messages.error(self.request, '保存に失敗しました')

        return super().form_invalid()
    
class QuestionlistView(generic.ListView):
    template_name="question_list.html"
    model = Question
    paginate_by = 10
    
class DetailQuestionView(generic.DetailView):
    model = Question
    template_name='question_detail.html'
    
    
