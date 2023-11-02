from django import  forms

from .models import  Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','content', 'time_create',)
        widgets ={
            'title':forms.TextInput(attrs={'class':'tieude123'}),
            'content':forms.Textarea(attrs={'class':'noidungabc'})
        }
class Send_email(forms.Form):
    title =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'hoangduy', 'id':'noidung'}))
    cc = forms.BooleanField()