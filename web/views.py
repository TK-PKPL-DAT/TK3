from django.shortcuts import render
from .models import UserAccount

def test_db_view(request):
    # Mengambil semua data dari tabel USER_ACCOUNT
    data_user = UserAccount.objects.all()
    return render(request, 'test_db.html', {'users': data_user})
