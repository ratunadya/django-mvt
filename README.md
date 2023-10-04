
# Tugas 2 PBP

![Logo Fasilkom UI](image-7.png)

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


***


# Tugas 3 PBP  

## Jawaban Pertanyaan  
  
### Perbedaan antara form ``POST`` dan ``GET`` dalam Django  

#### 1. Cara Kerja
- ``POST:`` _Browser_ membungkus data form -> Menulisnya dalam bentuk sandi untuk transmisi -> Mengirimnya ke server -> Menerima respon kembali   
- ``GET:`` GET membungkus data yg di-_submit_ dalam bentuk _string_ -> Menggunakan _string_ yang dibuat dalam pembuatan URL (terdiri dari alamat ke mana data akan dikirim serta _key_ dan _value_ data).   

#### 2. Penggunaan
- ``POST:`` _Request_ biasanya digunakan untuk mengirim data ke server, terutama untuk _request_ yang melibatkan modifikasi _state system_, seperti perubahan di dalam _database_ (menambahkan atau memperbarui entri _database_).

- ``GET:`` _Request_ biasanya digunakan untuk membaca atau mengambil data dari server (_read-only operations_), cocok untuk request yang tidak memengaruhi _state system_ dan _request_ seperti pencarian web karena URL yang merepresentasikan _request_ GET bisa di-_bookmark_, bagi, atau _submit_ ulang.

#### 3. Kapasitas
- ``POST:`` Tidak memiliki batasan kapasitas yang ketat untuk data yang dikirim (tergantung konfigurasi server).

- ``GET:``
Panjang URL terbatas sehingga jumlah data yang dapat dikirim terbatas. Akibatnya, GET kurang cocok untuk data dalam jumlah besar dan data biner.

#### 4. Keamanan
- ``POST:`` 
    - Lebih aman dan terkontrol untuk data sensitif, dipadukan dengan perlindungan lain seperti perlindungan CSRF Django.
    - Data _form_ tidak terlihat di URL, melainkan di _request body_.
- ``GET:``
    - Memiliki risiko keamanan (seperti risiko peniruan _request form_ untuk memperoleh akses ke bagian sensitif sistem). 
    - Data _form_ terlihat dalam bentuk teks biasa di URL, riwayat _browser_, dan log server sehingga tidak cocok untuk data sensitif seperti kata sandi. 

#### 5. HTTP Status
- ``POST:`` Ketika sukses, server mengembalikan kode status HTTP 201 (atau 200 (OK) tergantung implementasi aplikasi).
- ``GET:`` Jika data berhasil diambil, mengembalikan kode status HTTP 200 (OK).
  
### Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data  

|                                    **XML**                                   |                                            **JSON**                                            |                                                     **HTML**                                                     |
|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| Menyimpan dan menampilkan data  dalam bentuk _tree structure_                | Menyimpan dan menampilkan data  dalam bentuk pasangan _name_ dan  _value_ yang dipisahkan koma | Serupa dengan XML, tetapi umumnya menampilkan  data ke _end-user_ dalam bentuk visualisasi  dari data mentah     |
| Digunakan untuk menyimpan dan  bertukar data yang kompleks atau terstruktur  | Digunakan untuk menyimpan dan  bertukar data, memiliki format ringkas dan mudah dibaca         | Utamanya digunakan untuk menyajikan konten kepada _end-users_ dan secara umum bukan untuk pertukaran data mentah |
| Tidak mendukung penggunaan _array_                                           | Mendukung struktur data _array_                                                                | Mendukung struktur mirip _array_, yaitu _ordered list_ dan _unordered list_                                      |
| Menggunakan _start_ dan _end_ tag yang merepresentasikan data  dengan detail | Tidak menggunakan _end_ tag                                                                    | Menggunakan _start_ dan _end_ tag untuk mendefinisikan elemen dalam _web page_                                     |
| Mendukung penggunaan _namespaces_                                            | Tidak mendukung penggunaan _namespaces_ dan komentar                                           | Mendukung _namespaces_ secara terbatas (dalam konteks xhtml)                                                     |

### Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena:

#### 1. Sederhana dan Fleksibel
- JSON memungkinkan struktur data kompleks untuk ditampilkan dalam format pasangan _key-value_ dan _arrays_ yang ringkas dan mudah dibaca (_self-descriptive_ dan _human-readable_). 
- Format JSON secara _syntax_ identik dengan kode untuk membuat objek JavaScript. Karena kemiripan ini, program JavaScript dapat mengubah data JSON menjadi objek JavaScript dengan mudah. Hal ini akan memudahkan pengembang web yang menggunakan JavaScript sebagai bahasa skrip utama untuk aplikasi web mereka.
  
#### 2. Kompatibilitas
- Memiliki kompatibilitas dan interoperabilitas dengan berbagai bahasa, platform, dan framework.
- Didukung oleh banyak _browser_ modern, web _APIs_, dan web server. Hal ini memudahkan pertukaran data.
- Dapat digunakan dengan berbagai _library_ dan alat yang menyediakan fungsi untuk memvalidasi, mengurai, mengubah, dan memanipulasi data JSON (contoh: jQuery).

#### 3. Performa
- Ukurannya lebih kecil dan strukturnya lebih sederhana sehingga biasanya lebih cepat dan ringan dibandingkan XML.
- Tidak memiliki informasi yang tidak perlu yang dapat meningkatkan _overhead_ dan kompleksitas seperti pada XML (contoh: _closing tag_, _namespace_, dsb.).
- Dengan mengurangi _bandwidth_ dan waktu pemrosesan transfer dan manipulasi data, JSON dapat meningkatkan kecepatan dan daya tanggap aplikasi web. 

### Implementasi checklist secara step-by-step   
  
#### Membuat input form untuk menambahkan objek model pada app sebelumnya

- Membuat berkas ``forms.py`` dan mendefinisikan Class ``ItemForm`` yang menerima data item. Dalam kasus saya, ia menerima data item ``name``, ``amount``, ``goal_amount``, ``category``, ``description``.
- Membuat fungsi ``create_item`` dalam berkas ``views.`` untuk menghasilkan formulir yang dapat menambahkan data item baru ketika data di-_submit_. Data yang masuk akan disimpan ke dalam _database_.
- Mengubah fungsi ``show_main`` dalam ``views.py`` untuk mengambil dan menampilkan data item dari _database_.
- Menambah _path_ URL ke dalam ``urls.py`` agar aplikasi dapat mengakses ``create_item``.
- Membuat halaman ``create_item.html`` untuk menampilkan formulir input data produk.
- Menambahkan kode berikut untuk menampilkan data dalam bentuk tabel serta tombol "Buat Galang Dana" yang akan _redirect_ ke halaman form:

```
...
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Goal Amount</th>
            <th>Category</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.goal_amount}}</td>
                <td>{{item.category}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Buat Galang Dana
        </button>
    </a>

{% endblock content %}
```

  
#### Tambahkan 5 fungsi view untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML _by ID_, dan JSON by ID

**HTML**  
- Pada fungsi ``show_main`` di ``views.py``, membuat variabel baru bernama ``items`` yang menyimpan hasil _query_ dari data dengan meng-_assign_ ``Item.objects.all()``.
- Menambahkan _key_ ``‘items’`` dan _value_ ``items`` pada _dictionary_ ``context`` untuk mengirim data item ke tampilan.

**XML/JSON/XML by ID/JSON by JD**  
- Melakukan impor ``HttpResponse`` dan ``Serializer`` (digunakan untuk mentranslasi objek model).
- Membuat fungsi view ``show_[xml/json/xml_by_id/json_by_id]`` yang menerima parameter ``request``.
- Membuat variabel ``data`` yang menyimpan hasil _query_ dari data Item (dengan meng-_assign_ fungsi ``Item.objects.all()`` untuk XML dan JSON, ``.filter(pk=id)`` untuk XML JSON berdasarkan ID) dan menambahkan _return function_ berupa ``HttpResponse`` dengan parameter hasil _query_ yang sudah diserialisasi dan parameter ``content_type=“application/[xml/json]“``
- Mengimpor fungsi yang sudah dibuat
- Membuat _routing_ URL agar fungsi yang sudah diimpor dapat diakses

#### Membuat _routing_ URL untuk masing-masing ``views`` yang telah ditambahkan pada poin sebelumnya
  
Menambahkan fungsi path dalam berkas urls.py di direktori aplikasi sebagai berikut:

```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

masing-masing path akan mengarahkan URL ke fungsi view yang sesuai.

### Screenshot hasil akses URL pada Postman

#### HTML

![Screenshot hasil akses URL HTML](image-2.png)

#### XML

![Screenshot hasil akses URL XML](image-3.png)

#### JSON

![Screenshot hasil akses URL JSON](image-4.png)

#### XML _by ID_

![Screenshot hasil akses URL XML by ID](image-5.png)

#### JSON _by ID_

![Screenshot hasil akses URL JSON by ID](image-6.png)


***


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


***


# Tugas 5 PBP

## Jawaban Petanyaan

### Manfaat dari setiap _element selector_ dan waktu yang tepat untuk menggunakannya

_Element Selector_ adalah salah satu _selector_ pada CSS yang menjadikan elemen sebagai _selector_. Manfaat secara umum dari element selector adalah mengaplikasikan _style_ atau _declaration_ (_property_:_value_) yang sama kepada satu tipe elemen. _Element Selector_ akan meningkatkan efisiensi karena kita tidak perlu menspesifikkan tampilan yang sama satu persatu pada tiap _tag_ HTML yang sama. Beberapa variasi _element selector_ beserta manfaatnya antara lain:

|    **_Selector_**   |                                                                       **Manfaat dan Waktu Penggunaan**                                                                       |
|:-------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| element             | Ketika ingin men-_select_ semua elemen yang memiliki _tag_ HTML yang sama.                                                                                                   |
| element.class       | Ketika ingin men-_select_ semua elemen dengan _class_ tertentu (misal: `p.intro`, _class_=`intro`).                                                                          |
| element, element    | Ketika ingin men-_select_ masing-masing semua elemen dua _tag_ HTML yang dijadikan _selector_ (misal: div, p akan men-_select_ semua elemen `<div>` dan semua elemen `<p>`). |
| element element     | Ketika ingin men-_select_ semua elemen satu _tag_ HTML yang ada di dalam _tag_ HTML lainnya (_nested_).                                                                      |
| element1 > element2 | Ketika ingin men-_select_ semua element2, di mana _parent_-nya adalah element1.                                                                                              |
| element1 + element2 | Ketika butuh men-_select_ elemen2 pertama yang posisinya persis setelah element1.                                                                                            |
| element1 ~ element2 | Ketika butuh men-_select_ setiap elemen element2 yang didahului oleh elemen element1.                                                                                        |

Waktu yang tepat untuk menggunakan element selector adalah saat kita ingin mengaplikasikan tampilan yang sama kepada sebuah grup elemen secara bersamaan tanpa mementingkan karakteristik tertentu dari tag HTML selain fakta bahwa ia adalah elemen yang sama.

### HTML5 _Tag_ yang saya ketahui

|       **HTML5 _Tag_**       |                                                                                                                                 **Penjelasan**                                                                                                                                 |
|:---------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `<a>`                       | Singkatan dari “anchor tag”, menspesifikkan anchor. Biasanya digunakan bersama dengan attribute-nya yaitu href (hypertext reference) yang bisa membuat navigasi antara halaman web, tautan ke dokumen lain, atau bahkan tautan ke bagian yang berbeda dalam halaman yang sama. |
| `<abbr>`                    | Mendefinisikan singkatan atau akronim.                                                                                                                                                                                                                                         |
| `<address>`                 | Mendefinisikan kontak informasi pemilik dokumen. Biasanya di-_render_ dalam _italic_.                                                                                                                                                                                          |
| `<body>`                    | Mendefinisikan _body_ dokumen. Dalam sebuah dokumen HTML, hanya ada satu elemen _body_.                                                                                                                                                                                        |
| `<br>`                      | Menambahkan _single line break_. Merupakan salah satu _self-closing tag_ (_empty tag_).                                                                                                                                                                                        |
| `<button>`                  | Membuat tombol yang dapat diklik oleh pengguna.                                                                                                                                                                                                                                |
| `<div>`                     | Membuat sebuah grup elemen atau _section_ dalam dokumen.                                                                                                                                                                                                                       |
| `<nav>`                     | _Tag_ untuk mendefinisikan sekumpulan tautan navigasi.                                                                                                                                                                                                                         |
| `<footer>`                  | Mendefinisikan sebuah _footer_ dalam dokumen.                                                                                                                                                                                                                                  |
| `<h1>`, `<h2>`, ..., `<h6>` | Mendefinisikan _heading_. `<h1>` adalah _heading_ paling penting dan berukuran paling besar, menuju `<h6>`, ukuran _heading_ mengecil dan tingkat kepentingannya terakhir.                                                                                                     |

### Perbedaan antara _margin_ dan _padding_

***Margin*** mengontrol jarak antara _border_ dengan elemen lainnya (batas luar). Sementara itu, ***padding*** memberikan jarak di antara konten dan _border_ (batas dalam).

### Perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

|                                     **Tailwind CSS**                                     |                                   **Bootstrap**                                  |
|:----------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| Menawarkan pendekatan penggabungan kelas-kelas utilitas yang juga dapat digunakan ulang. | Menawarkan _template_ atau komponen siap-pakai.                                  |
| Menawarkan fleksibilitas dan kebebasan desain yang lebih tinggi.                         | Menghasilkan tampilan yang lebih konsisten.                                      |
| Cenderung memiliki _file_ CSS yang lebih kecil dibandingkan dengan Bootstrap.            | Cenderung memiliki _file_ CSS yang lebih besar dibandingkan dengan Tailwind CSS. |
| Memerlukan pemahaman akan kelas-kelas utilitas dan penggabungannya.                      | Lebih mudah digunakan oleh pemula.                                               |

Jika kita membutuhkan lebih banyak kontrol dalam kustomisasi tampilan dan memiliki penekanan lebih pada fleksibelitas serta kreaktivitas desain, Tailwind CSS dapat menjadi pilihan yang baik. Jika kita ingin mengembangkan proyek dengan cepat dan membutuhkan komponen yang  siap pakai dengan gaya konsisten, Bootstrap dapat menjadi pilihan yang baik.

### Implementasi _checklist_ di atas secara _step-by-step_

#### Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan Tailwind CSS

* Melakukan _install_ Tailwind menggunakan _Play CDN_ dengan menambahkan baris kode berikut pada `base.html`

```
 <script src="https://cdn.tailwindcss.com"></script>
 ```
* Menambahkan kode berikut pada `base.html`

```
<body class="bg-gradient-to-r from-cyan-500 to-blue-500">
```
