
# Tugas 2 PBP

![Logo Fasilkom UI](image.png)

Nama        : Ratu Nadya Anjania  
NPM         : 2206029752  
Kelas       : PBP F  
Kode Asdos  : FH  

## Tautan Adaptable  

Tautan: **[https://donate.adaptable.app/](https://donate.adaptable.app/)**.  

## Jawaban Pertanyaan  

### 1. Implementasi checklist pada soal secara step-by-step

#### Membuat sebuah proyek Django baru  

> - Buat repositori baru dan _folder_ (direktori lokal proyek).  
> - Setup repositori pada terminal/_command prompt_ direktori lokal yang sudah dibuat:  
>    - Inisiasi git, buat berkas README.md dalam direktori lokal proyek yang kemudian di-_track_ untuk di-_commit_ (_add_), buat _commit_, hubungkan repositori lokal dengan repositori di GitHub, simpan perubahan ke GitHub.  
> - Buat dan aktifkan _virtual environment_  
> - Buat _file_ `requirements.txt` berisi _dependencies_ dan pasang dengan perintah pip install -r requirements.txt  
> - Buat proyek Django bernama `django_mvt` dengan perintah django-admin startproject django_mvt .  

#### Membuat aplikasi dengan nama main pada proyek tersebut  

> - Buka _folder_ direktori utama, lalu terminal dari direktori tersebut  
> - Aktifkan virtual environment dan jalankan perintah python manage.py startapp main  

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main  

> - Buka _file_ `settings.py` pada _folder_ direktori proyek dan tambahkan 'main' pada daftar aplikasi yang ada di list INSTALLED_APPS  

#### Membuat model pada aplikasi main dengan nama Item yang memiliki atribut (name, amount, goal_amount, category, description)  

> - Buka _file_ `models.py` pada direktori aplikasi main dan buat _Class_ bernama Item  
> - Di dalam _Class_, buat:  
>    - Atribut wajib:  
>        name (CharField)  
>        amount (IntegerField)  
>        description (TextField)  
>    - Atribut tambahan:  
>        goal_amount (IntegerField)  
>        category (CharField)  
>    - _Tuple_ category_choices untuk _dropdown_ atribut category

#### Membuat fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu  

> Buat fungsi bernama `show_main` pada `views.py` dengan parameter request dan kembalian berupa objek HttpResponse dengan teks yang dirender yang selanjutnya di-assign ke template `main.html`. Fungsi ini memiliki dictionary `context` dengan key dan value yang tertera pada kode di bawah ini. Fungsi ini menggabungkan template dan context dictionary tersebut.  
```
def show_main(request):
    context = {
        'app_name': 'Aplikasi Pengelola Donasi',
        'name': 'Ratu Nadya A.',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
```

#### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py  

> - Tambah fungsi path dalam _file_ `urls.py` di direktori proyek di `urlpatterns` dengan argumen `('', include('main.urls'))` untuk mengarahkan ke _file_ `urls.py` di direktori aplikasi.  
> - Buat `urls.py` pada direktori aplikasi main dan tambahkan `urlpatterns` dengan `path` yang memiliki argumen seperti di bawah agar dapat menampilkan _file_ html yang akan dipanggil oleh fungsi yang telah dibuat pada `views.py`.  
```
urlpatterns = [
    path('', show_main, name='show_main')
] 
```

#### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat  

> - Buka terminal dan jalankan git add, commit, push  
> - Login pada adaptable, klik tombol New App, lalu Connect an Existing Repository  
> - Pilih basis aplikasi yang di-deploy (repositori proyek)  
> - Pilih deployment branch (main), template deployment (Python App Template), tipe basis data (PostgreSQL), dan versi python (3.11)  
> - Masukkan perintah `python manage.py migrate && gunicorn django-mvt.wsgi` pada Start Command  
> - Tuliskan nama aplikasi  
> - Centang HTTP Listener on Port  
> - Tekan tombol Deploy App, selesai :>  

#### Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan yang telah diberikan

> Tuliskan jawaban dari pertanyaan pada _file_ `README.md` yang telah dibuat. 
  
### 2. Bagan request client ke web aplikasi berbasis Django beserta respon dan penjelasan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](image-1.png)

**Penjelasan:**  
_Request_ yang masuk ke server Django akan diproses melalui _URL_, lalu diteruskan ke _view_ dan diproses. Jika peran database diperlukan, _view_ akan memanggil _query_ ke _model_ dan _database_ dan hasilnya akan dikembalikan ke _view_. Setelah itu, hasil tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan dan dikembalikan ke pengguna sebagai HTML response.  

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

_Virtual environment_ kita gunakan untuk mengisolasi _dependencies_ serta _package_ yang dibutuhkan oleh proyek. Hal ini dapat mencegah konflik antara penggunaan versi _dependencies_ kebutuhan proyek yang berbeda di komputer yang sama.  
  
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_, tetapi tindakan tersebut rawan berbagai masalah, seperti konflik antar-_dependencies_ seperti yang disebutkan, pengelolaan _dependencies_ yang lebih sulit, gangguan kinerja sistem operasi, dan sebagainya.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
  
Ketiganya merupakan pola desain atau arsitektur untuk pengembangan web untuk memisahkan komponen-komponen berdasarkan fungsinya.  
  
- **MVC (_Model, View, Controller_)**:  
    - ***Model***: Komponen inti dari arsitektur MVC yang bertanggung jawab terkait segala data, logika, dan aturan aplikasi.  
    - ***View***: Komponen yang menangani tampilan data kepada user yang berisi representasi data dari _model_.   
    - ***Controller***: Komponen yang menjembatani _model_ dan _view_. Komponen ini memanipulasi data dan me-_render_ _view_.  
- **MVT (_Model, View, Template_)**:  
    - ***Model***: Komponen pengatur dan pengelola data dan interaksinya, serta penghubung aplikasi dengan basis data.  
    - ***View***: Komponen logika utama yang menghubungkan model dan template dalam memproses _request_ dari _client_.  
    - ***Template***: Komponen untuk menangani _user interface_ atau mengatur tampilan yang berisi data dari _model_ yang didapat melalui _view_.  
- **MVVM (_Model, View, ViewModel_)**:  
    - ***Model***: Komponen nonvisual yang mengelola data.  
    - ***View***: Komponen yang menangani struktur dan tampilan yang dilihat oleh client, representasi model, dan menerima interaksi client.  
    - ***ViewModel***: Komponen penghubung antara _view_ dan _model_ yang mengimplementasikan perintah dan properti yang bisa menjadi sarana pengikatan data oleh _view_. Jika terdapat perubahan _state_, _ViewModel_ memberi informasi kepada _view_.  
  
Perbedaan ketiganya terletak dalam aspek sebagai berikut:
#### Komponen Mediator  
> MVC memiliki _controller_ yang menjadi perantara antara _model_ dan _view_. MVT menggunakan _view_ sebagai mediator antara _model_ dan _template_. Sementara itu, _ViewModel_ pada MVVM berperan sebagai mediator _model_ (data-logika) dan _view_ (UI). _ViewModel_ menyesuaikan data dari _model_ ke bentuk yang sesuai untuk _view_, dan _data-binding_ biasanya digunakan untuk memperbarui _view_ ketika data di _ViewModel_ berubah secara otomatis.  
  
#### Penggunaannya dalam pengembangan
> MVVM biasa digunakan dalam pengembangan sebuah sistem aplikasi dengan fokus utama penggunaan _User Interface_, terutama saat menggunakan _data-binding_. Di samping itu, MVC dan MVT dapat digunakan dalam pengembangan proyek web dengan Django. MVC juga biasa dipakai dalam pengembangan sistem _software_ yang lebih luas, seperti aplikasi desktop dan nonweb lainnya.  



# Tugas 4 PBP  

## Jawaban Pertanyaan  
  
### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah sebuah formulir untuk membuat pengguna baru. Impor formulir bawaan ini mempermudah pembuatan formulir pendaftaran pengguna. UserCreationForm memiliki 3 _fields_, yaitu username, password1, dan password2.

- **Kelebihan**:  
    - Memudahkan pembuatan formulir pendaftaran pengguna, tidak perlu membuat kode dari awal sehingga menghemat waktu dan tenaga.
    - Melakukan validasi input pengguna sesuai aturan yang ada.
  
- **Kekurangan**:  
    - Menyediakan _fields_ terbatas, untuk melakukan kustomisasi perlu membuat _subclass_ dari UserCreationForm.
    - Tampilan bawaan sederhana.
 
### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Dalam konteks Django, **autentikasi** merupakan sebuah proses verifikasi bahwa pengguna benar-benar merupakan pengguna sah/siapa yang mereka klaim, sedangkan **otorisasi** menentukan akses apa saja yang dimiliki oleh pengguna yang telah terautentikasi.

Keduanya penting karena mereka termasuk dalam dua proses **keamanan** esensial yang digunakan untuk melindungi sistem dan informasi. Dengan adanya autentikasi dan otorisasi, privasi data pengguna bisa terjaga, risiko ancaman aplikasi web (seperti _CSRF_, _SQL injection_, dsb.) bisa diminimalisasi, serta mengontrol akses pengguna dengan ketat.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
 
Dalam konteks aplikasi web, ***cookies*** adalah sejumlah kecil informasi yang dikirim oleh server web ke browser dan kemudian dikirim kembali oleh browser pada request halaman berikutnya. Dalam konteks penggunaan _cookies_ untuk mengelola data sesi oleh Django, Django menggunakan cookie untuk **mengatasi kondisi _stateless_ aplikasi web dengan menyimpan ID sesi** sehingga setiap kali pengguna mengirimkan _request_ ke server, ID sesi akan digunakan untuk mengidentifikasi sesi pengguna. Dalam kasus _login_, pengguna tidak perlu _login_ berulang kali setiap pindah halaman. Ketika pengguna berhasil _login_ dan sesi mereka dikelola dengan bantuan _cookies_, pengguna dapat tetap terautentikasi di berbagai halaman tanpa harus _login_ ulang setiap kali pengguna mengakses halaman baru.
 
### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Cookies sendiri tidak membahayakan keamanan, tetapi **penggunaan cookies memiliki risiko potensial yang harus diwaspadai**. Penjahat siber dapat memanfaatkan cookies untuk menyamar sebagai pengguna, mengumpulkan data sensitif, mengakses akun pengguna lain, dan sebagainya. Risiko potensial yang perlu diperhatikan, yaitu ancaman serangan aplikasi web seperti XSS, CSRF, _cookie poisoning_, dan sebagainya. Oleh karena itu, pengelolaan dan pengamanan _cookies_ perlu diawasi dengan baik.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Implementasi fungsi registrasi, _login_, dan _logout_ 
- Jalankan _virtual environment_.
- _Import_ ``UserCreationForm``, ``redirect``, dan ``messages`` (tahapan _register_), ``authenticate`` dan ``login`` (tahapan _login_), ``logout`` (tahapan _logout_) pada ``views.py``.
- Pada ``views.py`` juga, buat fungsi ``register``, ``login_user``, dan ``logout_user`` yang menerima parameter _request_ dan memanfaatkan hal-hal yang telah diimpor  (``UserCreationForm``, dst.).
- Buat berkas HTML untuk bagian _register_ dan _login_ dengan nama ``register.html`` dan ``login.html`` pada ``main/templates``. Fungsi yang telah dibuat tadi akan me-_render_ berkas html tersebut.
- Untuk _logout_, tambahkan _button logout_ di berkas ``main.html`` pada ``main/templates``.
- Impor fungsi-fungsi yang sudah dibuat pada ``urls.py`` di subdirektori ``main``.
- Tambahkan _path_ ke dalam ``urlpatterns`` agar fungsi dapat diakses.

#### Pembuatan dua akun pengguna dengan tiga _dummy data_

Register dua akun dengan dua kredensial (_username_, _password_) berbeda, lalu meng-_input_ 3 data baru dalam masing-masing akun.

#### Menghubungkan model ``Item`` dengan ``User``

- Impor ``User`` dalam ``models.py`` yang ada di subdirektori main.
- Menambahkan kode sebagai berikut yang mengasosiasikan satu item dengan satu user melalui _relationship_.
```
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
- Menambahkan kode berikut untuk mencegah Django menyimpan objek secara langsung ke _database_ serta menandakan objek milik pengguna yang sedang _login_.
```
...
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
- Menampilkan objek item yang terasosiasi dengan pengguna dengan menambahkan kode berikut pada fungsi ``show_main`` di ``views.py``
```
...
 products = Product.objects.filter(user=request.user)
 ...
 ```
 - Simpan perubahan dan lakukan migrasi.
 - Menetapkan _default value_ untuk _field user_ dengan memilih ``pilihan 1`` ketika muncul _error_ saat migrasi model.
 - Menetapkan _user_ dengan ID 1 dengan mengetik angka `1` lagi.
 - Melakukan migrasi.
 

####  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

- Impor ``datetime`` (``HttpResponseRedirect`` dan ``reverse`` sudah diimpor sebelumnya).
- Tambahkan cookie bernama ``last_login`` dengan mengganti kode dengan potongan kode berikut:
```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
- Menambahkan informasi _cookie_ pada respons yang akan ditampilkan dengan menambahkan kode berikut pada ``context``di ``show_main``:
```
'last_login': request.COOKIES['last_login'],
```
- Menampilkan data _last login_ dengan menambahkan kode mengenai keterangan sesi terakhir login pada ``main.html``.