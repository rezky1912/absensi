import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://absensiwajahjava-default-rtdb.firebaseio.com/"
})

ref = db.reference('Karyawan')

data = {
    "3320230804":
        {
            "name": "Pangestu Septiansyah",
            "divisi": "IT TEKNIS",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
    "2220230802":
        {
            "name": "Tri Buwono",
            "divisi": "IT TEKNIS",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "2220230803":
        {
            "name": "Rizki Perdana Affandi",
            "divisi": "IT TEKNIS",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "1120230803":
        {
            "name": "Stefan Widi Pratama",
            "divisi": "IT DESIGN",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "1120230802":
        {
            "name": "Yusuf Eko S",
            "divisi": "IT DESIGN",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "1120230801":
        {
            "name": "Hardianto Sholihin",
            "divisi": "IT DESIGN",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "3320230802":
        {
            "name": "Rio Ilyasar",
            "divisi": "IT DESIGN",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "4420230802":
        {
            "name": "Erick Prajogo",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "3320230801":
        {
            "name": "Frandika",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "4420230803":
        {
            "name": "Tiara Sylvia",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "5520220801":
        {
            "name": "Muh. Ikhsan",
            "divisi": "IT DESIGN",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "202312":
        {
            "name": "Johan",
            "divisi": "HRD",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "3320230803":
        {
            "name": "Shilvia Dewantari",
            "divisi": "IT MEDIA",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "4420230804":
        {
            "name": "Tara Azaria",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "4420230806":
        {
            "name": "Intan Nur Aini",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "4420230805":
        {
            "name": "Novi Aditya",
            "divisi": "IT CONTENT",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        },
        "2220230801":
        {
            "name": "Rezky",
            "divisi": "IT TEKNIS",
            "Tahun_Masuk": "2023",
            "total_absen": 0,
            "Jabatan": "Content",
            "tahun": 0,
            "kapan_terakhir_absen": "2023-08-14 08:23:20"
        }
        # "202318":
        # {
        #     "name": "Pangestu Septiansyah ",
        #     "divisi": "IT TEKNIS",
        #     "Tahun_Masuk": "2023",
        #     "total_absen": 0,
        #     "Jabatan": "Content",
        #     "tahun": 0,
        #     "kapan_terakhir_absen": "2023-08-14 08:23:20"
        # },
        # "202319":
        # {
        #     "name": "Pangestu Septiansyah ",
        #     "divisi": "IT TEKNIS",
        #     "Tahun_Masuk": "2023",
        #     "total_absen": 0,
        #     "Jabatan": "Content",
        #     "tahun": 0,
        #     "kapan_terakhir_absen": "2023-08-14 08:23:20"
        # },
        # "202320":
        # {
        #     "name": "Pangestu Septiansyah ",
        #     "divisi": "IT TEKNIS",
        #     "Tahun_Masuk": "2023",
        #     "total_absen": 0,
        #     "Jabatan": "Content",
        #     "tahun": 0,
        #     "kapan_terakhir_absen": "2023-08-14 08:23:20"
        # }
}


for key, value in data.items():
    ref.child(key).set(value)
