# from unicodedata import category
from django.shortcuts import render , redirect ,HttpResponse ,HttpResponseRedirect
from django.views.generic import View
from django.views.generic import ListView , DetailView
from app.forms import BookForm, IssueBookForm, MemberProfile
from app.models import *
from datetime import date
# Create your views here.



def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'app/home.html')

def memberclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'app/member_click.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'app/admin_click.html')



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'app/admin_walls.html')
    else:
        member = Member.objects.all()
        return render(request,'app/member_wall.html', {'member':member})    

#Add Books
class BookView(View):

    def get(self ,request):
        form = BookForm()
        return render(request, 'app/add_book.html' , {'form':form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            isbn = form.cleaned_data['isbn']
            category = form.cleaned_data['category']

            books = Book(title=title,author=author,isbn=isbn,category=category)
            books.save()
            alert = True
            return redirect('book-list')
        return render(request , 'app/add_book.html',{'form':form})

#View books    

class BookList(ListView):
    model = Book
    template_name = 'app/list_book.html'

def MemberList(request):
    members = Member.objects.all()
    return render(request , 'app/list_member.html' , {'members':members})



class Issue_bookView(View):
    def get(self , request):
        form = IssueBookForm()
        return render(request , 'app/issue_book.html' , {'form':form})
    
    def post(self , request):
        form = IssueBookForm(request.POST)
        if form.is_valid():
            si = form.cleaned_data['member_id']
            isbn = form.cleaned_data['isbn']

            obj = IssuedBook(member_id=si , isbn=isbn)
            obj.save()
            alert = True
            return render(request, "app/issue_book.html", {'obj':obj, 'alert':alert})
        return render(request, "app/issue_book.html", {'form':form})

def delete_book(request, pk):
    books = Book.objects.filter(id=pk)
    books.delete()
    return redirect("/view_books")



def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(Book.objects.filter(isbn=i.isbn))
        members = list(Member.objects.filter(user=i.member_id))
        i=0
        for l in books:
            t=(members[i].user,members[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "app/view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})

def member_issued_books(request):
    member = Member.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(member_id=member[0].user_id)
    li1 = []
    li2 = []

    for i in issuedBooks:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            t=(request.user.id, request.user.get_full_name, book.name,book.author)
            li1.append(t)

        days=(date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>15:
            day=d-14
            fine=day*5
        t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
        li2.append(t)
    return render(request,'app/member_issued_books.html',{'li1':li1, 'li2':li2})

# class ProfileView(DetailView):
#     model = Member

#     template_name = 'app/profile.html'

def ProfileView(request , pk):
    book = Book.objects.get(user_id=pk) 
    member = Member.objects.get(id=pk)
    context = {'member':member , 'book':book}
    return render(request , 'app/profile.html' , context)

class ProfileFormView(View):
    def get(self , request):
        pk = request.user.id
        if  Member.objects.filter(user_id=pk):                  # If request.user is New user so it will have to fill up profile details first
            return redirect('home')
        else:
            form = ProfileFormView()   
        context = {'form':form}
        return render(request , 'app/profile_form.html' , context)

    def post(self , request):
        form = MemberProfile(request.POST)
        if form.is_valid():
            # n14 = request.user
            # n11 = form.cleaned_data['first_name']
            # n12 = form.cleaned_data['last_name']
            # n2 = form.cleaned_data['profile_pic']
            # n3 = form.cleaned_data['std']
            # n4 = form.cleaned_data['roll_no']
            # n5 = form.cleaned_data['phone']
            # n6 = form.cleaned_data['branch']

            data = form.save(commit=False)
            data.user = request.user
            data.save()

            # member = Member(user = n14,first_name=n11,last_name=n12,profile_pic=n2,std=n3,roll_no=n4,phone=n5,branch=n6)
            # member.save()
            return redirect('home')
        return render(request , 'app/profile_form.html',{'form':form})

def delete_member(request, pk):
    member = Member.objects.filter(id=pk)
    member.delete()
    return redirect("member-list")




    