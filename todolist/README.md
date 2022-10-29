Link Heroku :
 https://tugas-pbp-idham.herokuapp.com/todolist berisi halaman utama yang memuat tabel task.
 https://tugas-pbp-idham.herokuapp.com/todolist/login berisi form login.
 https://tugas-pbp-idham.herokuapp.com/todolist/register berisi form registrasi akun.
 https://tugas-pbp-idham.herokuapp.com/todolist/create-task berisi form pembuatan task.
 https://tugas-pbp-idham.herokuapp.com/todolist/logout berisi mekanisme logout.

Jawaban Tugas 4 :
CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban.

Kita dapat membuat form tanpa menggunakan format {{form.as_table}}. Dengan menggunakan tag form setelah itu membuat tag input yang berisi name sebagai variabel.

Alur dari pengisian form yaitu user mengisi input formnya setelah mengklik submit form yang mana nantinya submit melakukan request POST ke url yang telah dibuat. Setelah itu isi dari form akan disimpan pada database melalui models object create atau bisa dilakukan dengan form.save()