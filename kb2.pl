truong('KHTN').
to_chuc('DHQGHCM').

truc_thuoc('KHTN', 'DHQGHCM').

% Khoa CNTT.
khoa('CNTT').

truc_thuoc('CNTT', 'DH KHTN').

nam_thanh_lap('CNTT',1995).

phong('CNTT','I53').
bo_mon('Khoa hoc may tinh').
phong('Khoa hoc may tinh', 'I81').
bo_mon('Cong nghe tri thuc').
phong('Cong nghe tri thuc', 'I63').
bo_mon('Thi giac may tinh va dieu khien hoc thong minh').
phong('Thi giac may tinh va dieu khien hoc thong minh', 'I72').
bo_mon('He thong thong tin').
phong('He thong thong tin', 'I84').
bo_mon('Mang may tinh va Vien thong').
phong('Mang may tinh va Vien thong', 'I74').
bo_mon('Cong nghe phan mem').
phong('Cong nghe phan mem', 'I82').

truc_thuoc('Cong nghe tri thuc', 'CNTT').
truc_thuoc('Khoa hoc may tinh', 'CNTT').
truc_thuoc('Cong nghe phan mem', 'CNTT').
truc_thuoc('Thi giac may tinh va dieu khien hoc thong minh', 'CNTT').
truc_thuoc('Mang may tinh va Vien thong', 'CNTT').
truc_thuoc('He thong thong tin', 'CNTT').

nam_thanh_lap('Cong nghe tri thuc', 2009).
nam_thanh_lap('Khoa hoc may tinh', 2010).
nam_thanh_lap('Thi giac may tinh va dieu khien hoc thong minh', 2010).
nam_thanh_lap('Cong nghe phan mem', 2010).
nam_thanh_lap('Mang may tinh va Vien thong', 1998).


nganh('He thong thong tin').
truc_thuoc('He thong thong tin','CNTT').

nganh('Khoa hoc may tinh').
truc_thuoc('Khoa hoc may tinh','CNTT').

nganh('Ky thuat phan mem').
truc_thuoc('Ky thuat phan mem','CNTT').

nganh('Cong nghe thong tin').
truc_thuoc('Cong nghe thong tin','CNTT').


chuyen_nganh('Ky thuat phan mem').
truc_thuoc('Ky thuat phan mem','Ky thuat phan mem').

chuyen_nganh('Khoa hoc may tinh').
truc_thuoc('Khoa hoc may tinh', 'Khoa hoc may tinh').
chuyen_nganh('Cong nghe tri thuc').
truc_thuoc('Cong nghe tri thuc', 'Khoa hoc may tinh').
chuyen_nganh('Thi giac may tinh va dieu khien hoc thong minh').
truc_thuoc('Thi giac may tinh va dieu khien hoc thong minh', 'Khoa hoc may tinh').
chuyen_nganh('An toan thong tin').
truc_thuoc('An toan thong tin', 'Khoa hoc may tinh').
chuyen_nganh('Khoa hoc du lieu').
truc_thuoc('Khoa hoc du lieu', 'Khoa hoc may tinh').

chuyen_nganh('He thong thong tin').
truc_thuoc('He thong thong tin','He thong thong tin').

chuyen_nganh('Mang may tinh').
truc_thuoc('Mang may tinh', 'Cong nghe thong tin').
chuyen_nganh('Cong nghe thong tin').
truc_thuoc('Cong nghe thong tin', 'Cong nghe thong tin').


truong_khoa('Dinh Ba Tien', 'CNTT').

truong_bo_mon('Nguyen Van Vu', 'Cong nghe phan mem').
truong_bo_mon('Le Hoai Bac', 'Khoa hoc may tinh').
truong_bo_mon('Pham Nguyen Cuong', 'He thong thong tin').
truong_bo_mon('Tran Trung Dung', 'Mang may tinh va Vien thong').
truong_bo_mon('Ly Quoc Ngoc','Thi giac may tinh va dieu khien hoc thong minh').
truong_bo_mon('Nguyen Dinh Thuc', 'Cong nghe tri thuc').

pho_khoa('Lam Quang Vu', 'CNTT').
pho_khoa('Van Chi Nam', 'CNTT').
pho_khoa('Nguyen Van Vu', 'CNTT').
pho_bo_mon('Le Ngoc Thanh', 'Khoa hoc may tinh').
pho_bo_mon('Dinh Dien', 'Cong nghe tri thuc').
pho_bo_mon('Nguyen Tran Minh Thu', 'He thong thong tin').
pho_bo_mon('Nguyen Thi Minh Tuyen', 'Cong nghe phan mem').
pho_bo_mon('Huynh Thuy Bao Tran', 'Mang may tinh va Vien thong').
pho_bo_mon('Tran Thai Son', 'Thi giac may tinh va dieu khien hoc thong minh').

giang_vien('Le Hoai Bac').
truc_thuoc('Le Hoai Bac','Khoa hoc may tinh').
giang_vien('Nguyen Dinh Thuc').
truc_thuoc('Nguyen Dinh Thuc','Cong nghe tri thuc').
giang_vien('Dinh Dien').
truc_thuoc('Dinh Dien','Cong nghe tri thuc').
giang_vien('Ly Quoc Ngoc').
truc_thuoc('Ly Quoc Ngoc','Khoa hoc may tinh').
truc_thuoc('Ly Quoc Ngoc','Thi giac may tinh va dieu khien hoc thong minh').
giang_vien('Dinh Ba Tien').
truc_thuoc('Dinh Ba Tien','Cong nghe phan mem').
giang_vien('Lam Quang Vu').
truc_thuoc('Lam Quang Vu','Cong nghe phan mem').
giang_vien('Van Chi Nam').
truc_thuoc('Van Chi Nam','Cong nghe phan mem').
giang_vien('Nguyen Van Vu').
truc_thuoc('Van Chi Nam','Cong nghe phan mem').
giang_vien('Le Ngoc Thanh').
truc_thuoc('Le Ngoc Thanh','Khoa hoc may tinh').
giang_vien('Nguyen Tran Minh Thu').
truc_thuoc('Nguyen Tran Minh Thu','He thong thong tin').
giang_vien('Pham Nguyen Cuong').
truc_thuoc('Pham Nguyen Cuong','He thong thong tin').

giang_vien('Tran Thai Son').
truc_thuoc('Tran Thai Son','Thi giac may tinh va dieu khien hoc thong minh').

giang_vien('Nguyen Thi Minh Tuyen').
truc_thuoc('Nguyen Thi Minh Tuyen','Cong nghe phan mem').

giang_vien('Tran Trung Dung').
truc_thuoc('Tran Trung Dung','Mang may tinh va Vien thong').

giang_vien('Huynh Thi Bao Tran').
truc_thuoc('Huynh Thi Bao Tran','Mang may tinh va Vien thong').

hoc_ham('Le Hoai Bac','GS').
hoc_ham('Nguyen Dinh Thuc','PGS').
hoc_ham('Dinh Dien','PGS').
hoc_ham('Ly Quoc Ngoc','PGS').

hoc_vi('Dinh Ba Tien','TS').
hoc_vi('Lam Quang Vu','TS').
hoc_vi('Van Chi Nam','ThS').
hoc_vi('Nguyen Van Vu','TS').
hoc_vi('Le Ngoc Thanh','TS').
hoc_vi('Le Hoai Bac','TS').
hoc_vi('Dinh Dien','TS').
hoc_vi('Nguyen Dinh Thuc','TS').
hoc_vi('Nguyen Tran Minh Thu','TS').
hoc_vi('Pham Nguyen Cuong','TS').
hoc_vi('Ly Quoc Ngoc','TS').
hoc_vi('Tran Thai Son','TS').
hoc_vi('Nguyen Thi Minh Tuyen','TS').
hoc_vi('Tran Trung Dung','TS').
hoc_vi('Huynh Thi Bao Tran','TS').

nam('Dinh Ba Tien').
nam('Lam Quang Vu').
nam('Van Chi Nam').
nam('Nguyen Van Vu').
nam('Le Hoai Bac').
nam('Le Ngoc Thanh').
nam('Nguyen Dinh Thuc').
nam('Dinh Dien').
nam('Pham Nguyen Cuong').
nam('Ly Quoc Ngoc').
nam('Tran Thai Son').
nam('Tran Trung Dung').
nu('Nguyen Tran Minh Thu').
nu('Huynh Thi Bao Tran').
nu('Nguyen Thi Minh Tuyen').

% Khoa Vat ly - Vat ly ky thuat.
khoa('Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly - Vat ly ky thuat', 'DH KHTN').
bo_mon('Vat ly Tin hoc').
bo_mon('Vat ly Ly thuyet').
bo_mon('Vat ly Ung dung').
bo_mon('Vat ly Dia cau').
bo_mon('Vat ly Dien tu').
bo_mon('Vat ly Chat ran').
bo_mon('Vat ly Hat nhan').
bo_mon('Hai duong hoc - Khi tuong - Thuy van').
truc_thuoc('Vat ly Tin hoc', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Ly thuyet', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Ung dung', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Dia cau', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Dien tu', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Chat ran', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Vat ly Hat nhan', 'Vat ly - Vat ly ky thuat').
truc_thuoc('Hai duong hoc - Khi tuong - Thuy van', 'Vat ly - Vat ly ky thuat').

giang_vien('Le Vu Tuan Hung').
giang_vien('Huynh Truc Phuong').
giang_vien('Huynh Van Tuan').
giang_vien('Nguyen Quoc Khanh').
giang_vien('Nguyen Thanh Van').
giang_vien('Nguyen Van Hieu').
giang_vien('Nguyen Chi Nhan').
giang_vien('Tran Quang Trung').
giang_vien('Chau Van Tao').
giang_vien('Truong Thi Hong Loan').
giang_vien('Vo Luong Hong Phuoc').

hoc_ham('Le Vu Tuan Hung','PGS').
hoc_ham('Huynh Truc Phuong','PGS').
hoc_ham('Huynh Van Tuan','PGS').
hoc_ham('Nguyen Quoc Khanh','PGS').
hoc_ham('Nguyen Thanh Van','PGS').
hoc_ham('Nguyen Van Hieu','PGS').
hoc_ham('Tran Quang Trung','PGS').
hoc_ham('Chau Van Tao','GS').
hoc_ham('Vo Luong Hong Phuoc','PGS').

hoc_vi('Le Vu Tuan Hung','TS').
hoc_vi('Huynh Truc Phuong','TS').
hoc_vi('Huynh Van Tuan','TS').
hoc_vi('Nguyen Quoc Khanh','TS').
hoc_vi('Nguyen Thanh Van','TS').
hoc_vi('Nguyen Van Hieu','TS').
hoc_vi('Nguyen Chi Nhan','ThS').
hoc_vi('Tran Quang Trung','TS').
hoc_vi('Chau Van Tao','TS').
hoc_vi('Truong Thi Hong Loan','TS').
hoc_vi('Vo Luong Hong Phuoc','TS').

truong_khoa('Le Vu Tuan Hung','Vat ly - Vat ly ky thuat').
pho_khoa('Huynh Truc Phuong','Vat ly - Vat ly ky thuat').
pho_khoa('Huynh Van Tuan','Vat ly - Vat ly ky thuat').

truong_bo_mon('Huynh Van Tuan','Vat ly Tin hoc').
truong_bo_mon('Nguyen Quoc Khanh','Vat ly Ly thuyet').
truong_bo_mon('Le Vu Tuan Hung','Vat ly Ung dung').
truong_bo_mon('Nguyen Thanh Van','Vat ly Dia cau').
truong_bo_mon('Nguyen Van Hieu','Vat ly Dien tu').
pho_bo_mon('Nguyen Chi Nhan','Vat ly Dien tu').
truong_bo_mon('Tran Quang Trung','Vat ly Chat ran').
truong_bo_mon('Chau Van Tao','Vat ly Hat nhan').
pho_bo_mon('Truong Thi Hong Loan','Vat ly Hat nhan').
truong_bo_mon('Vo Luong Hong Phuoc','Hai duong hoc - Khi tuong - Thuy van').


% Khoa Toan Tin hoc.
khoa('Toan - Tin hoc').

truc_thuoc('Toan - Tin hoc', 'DH KHTN').

bo_mon('Ung dung tin hoc').
bo_mon('Xac suat thong ke').
bo_mon('Dai so').
bo_mon('Giai tich').
bo_mon('Co hoc').
bo_mon('Toi uu va He thong').
bo_mon('Giao duc Toan hoc').
bo_mon('Tai Chinh Dinh Luong').

truc_thuoc('Ung dung tin hoc', 'Toan - Tin hoc').
truc_thuoc('Xac suat thong ke', 'Toan - Tin hoc').
truc_thuoc('Dai so', 'Toan - Tin hoc').
truc_thuoc('Giai tich', 'Toan - Tin hoc').
truc_thuoc('Co hoc', 'Toan - Tin hoc').
truc_thuoc('Toi uu va He thong', 'Toan - Tin hoc').
truc_thuoc('Giao duc Toan hoc', 'Toan - Tin hoc').
truc_thuoc('Tai Chinh Dinh Luong', 'Toan - Tin hoc').

giang_vien('Huynh Quang Vu').
giang_vien('Vo Duc Cam Hai').

giang_vien('Pham The Bao').
truc_thuoc('Pham The Bao', 'Ung dung tin hoc').

giang_vien('Dang Duc Trong').
truc_thuoc('Dang Duc Trong', 'Xac suat thong ke').

giang_vien('Mai Hoang Bien').
truc_thuoc('Mai Hoang Bien', 'Dai so').

giang_vien('Huynh Quang Vu').
truc_thuoc('Huynh Quang Vu', 'Giai tich').

giang_vien('Trinh Anh Ngoc').
truc_thuoc('Trinh Anh Ngoc', 'Co hoc').

giang_vien('Nguyen Le Hoang Anh').
truc_thuoc('Nguyen Le Hoang Anh', 'Toi uu va He thong').

giang_vien('Nguyen Viet Dong').
truc_thuoc('Nguyen Viet Dong', 'Giao duc Toan').

giang_vien('Dinh Ngoc Thanh').
truc_thuoc('Dinh Ngoc Thanh', 'Tai chinh Dinh luong').


hoc_ham('Pham The Bao','PGS').
hoc_ham('Dang Duc Trong','GS').
hoc_ham('Dinh Ngoc Thanh','PGS').
hoc_vi('Huynh Quang Vu','TS').
hoc_vi('Nguyen Le Hoang Anh','TS').
hoc_vi('Vo Duc Cam Hai','ThS').
hoc_vi('Pham The Bao','TS').
hoc_vi('Dang Duc Trong','TS').
hoc_vi('Mai Hoang Bien','TS').
hoc_vi('Trinh Anh Ngoc','TS').
hoc_vi('Nguyen Viet Dong','TS').
hoc_vi('Dinh Ngoc Thanh','TS').

truong_khoa('Huynh Quang Vu','Toan - Tin hoc').
pho_khoa('Nguyen Le Hoang Anh','Toan - Tin hoc').
pho_khoa('Vo Duc Cam Hai','Toan - Tin hoc').
truong_bo_mon('Pham The Bao','Ung dung tin hoc').
truong_bo_mon('Dang Duc Trong','Xac suat thong ke').
truong_bo_mon('Mai Hoang Bien','Dai so').
truong_bo_mon('Huynh Quang Vu','Giai tich').
truong_bo_mon('Trinh Anh Ngoc','Co hoc').
truong_bo_mon('Nguyen Le Hoang Anh','Toi uu va He thong').
truong_bo_mon('Nguyen Viet Dong','Giao duc Toan hoc').
truong_bo_mon('Dinh Ngoc Thanh','Tai chinh Dinh luong').


% Khoa Dien tu Vien thong.
khoa('Dien tu - Vien thong').
truc_thuoc('Dien tu - Vien thong', 'DH KHTN').
bo_mon('Dien tu').
bo_mon('Vien thong va Mang').
bo_mon('May tinh va He thong nhung').
truc_thuoc('Dien tu', 'Dien tu - Vien thong').
truc_thuoc('Vien thong va Mang', 'Dien tu - Vien thong').
truc_thuoc('May tinh va He thong nhung', 'Dien tu - Vien thong').

giang_vien('Huynh Huu Thuan').
truc_thuoc('Huynh Huu Thuan', 'May tinh va He thong nhung').

giang_vien('Cao Tran Bao Thuong').
truc_thuoc('Cao Tran Bao Thuong', 'May tinh va He thong nhung').

giang_vien('Bui Trong Tu').
truc_thuoc('Bui Trong Tu', 'Dien tu').

giang_vien('Dang Le Kha').
truc_thuoc('Dang Le Kha', 'Vien thong va Mang').

nam('Huynh Huu Thuan').
nam('Cao Tran Bao Thuong').
nam('Bui Trong Tu').
nam('Dang Le Kha').

hoc_vi('Huynh Huu Thuan','TS').
hoc_vi('Cao Tran Bao Thuong','ThS').
hoc_vi('Bui Trong Tu','TS').
hoc_vi('Dang Le Kha','TS').

truong_khoa('Huynh Huu Thuan','Dien tu - Vien thong').
pho_khoa('Cao Tran Bao Thuong','Dien tu - Vien thong').
pho_khoa('Bui Trong Tu','Dien tu - Vien thong').

truong_bo_mon('Bui Trong Tu','Dien tu').
truong_bo_mon('Dang Le Kha','Vien thong va Mang').
truong_bo_mon('Huynh Huu Thuan','May tinh va He thong nhung').


% Khoa Hoa hoc.
khoa('Hoa hoc').
truc_thuoc('Hoa hoc', 'DH KHTN').
bo_mon('Hoa Phan Tich').
bo_mon('Vo co va Ung dung').
bo_mon('Huu co').
bo_mon('Hoa ly').
bo_mon('Hoa hoc Polymer').
truc_thuoc('Hoa Phan Tich', 'Hoa hoc').
truc_thuoc('Vo co va Ung dung', 'Hoa hoc').
truc_thuoc('Huu co', 'Hoa hoc').
truc_thuoc('Hoa ly', 'Hoa hoc').
truc_thuoc('Hoa hoc Polymer', 'Hoa hoc').

giang_vien('Nguyen Thi Thanh Mai').
hoc_ham('Nguyen Thi Thanh Mai','PGS').
hoc_vi('Nguyen Thi Thanh Mai','TS').
nu('Nguyen Thi Thanh Mai').

giang_vien('Nguyen Cong Tranh').
hoc_vi('Nguyen Cong Tranh','TS').
nam('Nguyen Cong Tranh').

giang_vien('Nguyen Thu Huong').
hoc_vi('Nguyen Thu Huong','ThS').
nu('Nguyen Thu Huong').

giang_vien('Nguyen Van Dong').
hoc_ham('Nguyen Van Dong','PGS').
hoc_vi('Nguyen Van Dong','TS').
nam('Nguyen Van Dong').

giang_vien('Le Tien Khoa').
hoc_vi('Nguyen Van Dong','TS').
nam('Le Tien Khoa').

giang_vien('Nguyen Trung Nhan').
hoc_ham('Nguyen Trung Nhan','PGS').
hoc_vi('Nguyen Trung Nhan','TS').
nam('Nguyen Trung Nhan').

giang_vien('Ton That Quang').
hoc_vi('Ton That Quang','TS').
nam('Ton That Quang').

giang_vien('Nguyen Thai Hoang').
hoc_ham('Nguyen Thai Hoang','PGS').
hoc_vi('Nguyen Thai Hoang','TS').
nam('Nguyen Thai Hoang').

giang_vien('Ho Pham Anh Vu').
hoc_vi('Ho Pham Anh Vu','ThS').
nam('Ho Pham Anh Vu').


giang_vien('Hoang Ngoc Cuong').
hoc_ham('Hoang Ngoc Cuong','PGS').
hoc_vi('Hoang Ngoc Cuong','TS').
nam('Hoang Ngoc Cuong').

truong_khoa('Nguyen Thi Thanh Mai','Hoa hoc').
pho_khoa('Nguyen Cong Tranh','Hoa hoc').
pho_khoa('Nguyen Thu Huong','Hoa hoc').
truong_bo_mon('Nguyen Van Dong','Hoa Phan Tich').
truong_bo_mon('Le Tien Khoa','Vo co va Ung dung').
truong_bo_mon('Nguyen Trung Nhan','Huu co').
pho_bo_mon('Ton That Quang','Huu co').
truong_bo_mon('Nguyen Thai Hoang','Hoa ly').
pho_bo_mon('Ho Pham Anh Vu','Hoa ly').
truong_bo_mon('Hoang Ngoc Cuong','Hoa hoc Polymer').


% Khoa Sinh hoc - Cong nghe sinh hoc.
khoa('Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Sinh hoc - Cong nghe sinh hoc', 'DH KHTN').
bo_mon('CNSH Phan tu va MT').
bo_mon('Sinh ly Thuc vat').
bo_mon('Sinh hoa').
bo_mon('Di truyen').
bo_mon('CNSH Thuc vat va Chuyen hoa SH').
bo_mon('Vi sinh').
bo_mon('Sinh ly hoc va Cong nghe Sinh hoc Dong vat').
bo_mon('Sinh thai va Sinh hoc Tien hoa').
truc_thuoc('CNSH Phan tu va MT', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Sinh ly Thuc vat', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Sinh hoa', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Di truyen', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('CNSH Thuc vat va Chuyen hoa SH', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Vi sinh', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Sinh ly hoc va Cong nghe Sinh hoc Dong vat', 'Sinh hoc - Cong nghe sinh hoc').
truc_thuoc('Sinh thai va Sinh hoc Tien hoa', 'Sinh hoc - Cong nghe sinh hoc').

giang_vien('Nguyen Tri Nhan').
truong_khoa('Nguyen Tri Nhan','Sinh hoc - Cong nghe sinh hoc').
hoc_vi('Nguyen Tri Nhan','TS').
nam('Nguyen Tri Nhan').

giang_vien('Quach Ngo Diem Phuong').
pho_khoa('Quach Ngo Diem Phuong','Sinh hoc - Cong nghe sinh hoc').
truong_bo_mon('Quach Ngo Diem Phuong', 'CNSH Thuc vat va Chuyen hoa SH').
hoc_ham('Quach Ngo Diem Phuong','PGS').
hoc_vi('Quach Ngo Diem Phuong','TS').
nu('Quach Ngo Diem Phuong').

giang_vien('Tran Van Hieu').
pho_khoa('Tran Van Hieu','Sinh hoc - Cong nghe sinh hoc').
pho_bo_mon('Tran Van Hieu', 'CNSH Phan tu va MT').
hoc_ham('Tran Van Hieu','PGS').
hoc_vi('Tran Van Hieu','TS').
nam('Tran Van Hieu').

giang_vien('Dang Thi Phuong Thao').
truong_bo_mon('Dang Thi Phuong Thao', 'CNSH Phan tu va MT').
hoc_ham('Dang Thi Phuong Thao','PGS').
hoc_vi('Dang Thi Phuong Thao','TS').
nu('Dang Thi Phuong Thao').

giang_vien('Tran Thanh Huong').
truong_bo_mon('Tran Thanh Huong', 'Sinh ly Thuc vat').
hoc_ham('Tran Thanh Huong','PGS').
hoc_vi('Tran Thanh Huong','TS').
nu('Tran Thanh Huong').

giang_vien('Ngo Dai Nghiep').
truong_bo_mon('Ngo Dai Nghiep', 'Sinh hoa').
hoc_ham('Ngo Dai Nghiep','PGS').
hoc_vi('Ngo Dai Nghiep','TS').
nam('Ngo Dai Nghiep').

giang_vien('Nguyen Thuy Vy').
truong_bo_mon('Nguyen Thuy Vy', 'Di truyen').
hoc_vi('Nguyen Thuy Vy','TS').
nu('Nguyen Thuy Vy').

giang_vien('Nguyen Duc Hoang').
truong_bo_mon('Nguyen Duc Hoang', 'Vi sinh').
hoc_ham('Nguyen Duc Hoang','PGS').
hoc_vi('Nguyen Duc Hoang','TS').
nam('Nguyen Duc Hoang').

giang_vien('Tran Le Bao Ha').
truong_bo_mon('Tran Le Bao Ha', 'Sinh ly hoc va Cong nghe Sinh hoc Dong vat').
hoc_ham('Tran Le Bao Ha','PGS').
hoc_vi('Tran Le Bao Ha','TS').
nu('Tran Le Bao Ha').

giang_vien('Nguyen Thi Kim Dung').
truong_bo_mon('Nguyen Thi Kim Dung', 'Sinh thai va Sinh hoc Tien hoa').
hoc_vi('Nguyen Thi Kim Dung','TS').
nu('Nguyen Thi Kim Dung').

% Khoa Dia chat.
khoa('Dia chat').
truc_thuoc('CNTT', 'DH KHTN').
bo_mon('Dia chat bien va Dau khi').
bo_mon('Dia chat co so').
bo_mon('Dia chat Thuy van - Dia chat cong trinh').
bo_mon('Thach hoc va Khoang san').

truc_thuoc('Dia chat bien va Dau khi', 'Dia chat').
truc_thuoc('Dia chat co so', 'Dia chat').
truc_thuoc('Dia chat Thuy van - Dia chat cong trinh', 'Dia chat').
truc_thuoc('Thach hoc va Khoang san', 'Dia chat').

giang_vien('Pham Trung Hieu').
truong_khoa('Pham Trung Hieu', 'Dia chat').
hoc_ham('Pham Trung Hieu','PGS').
hoc_vi('Pham Trung Hieu','TS').
nam('Pham Trung Hieu').

giang_vien('Tran Thi Hoang Ha').
pho_khoa('Tran Thi Hoang Ha','Dia chat').
hoc_vi('Tran Thi Hoang Ha','TS').
nu('Tran Thi Hoang Ha').

giang_vien('Le Duc Phuc').
truong_bo_mon('Le Duc Phuc','Dia chat bien va Dau khi').
hoc_ham('Le Duc Phuc','GVC').
hoc_vi('Le Duc Phuc','TS').
nam('Le Duc Phuc').

giang_vien('Ngo Thi Phuong Uyen').
truong_bo_mon('Ngo Thi Phuong Uyen','Dia chat co so').
hoc_ham('Ngo Thi Phuong Uyen','GVC').
hoc_vi('Ngo Thi Phuong Uyen','ThS').
nu('Ngo Thi Phuong Uyen').

giang_vien('Ngo Minh Thien').
truong_bo_mon('Ngo Minh Thien','Dia chat Thuy van - Dia chat cong trinh').
hoc_ham('Ngo Minh Thien','GVC').
hoc_vi('Ngo Minh Thien','ThS').
nam('Ngo Minh Thien').

giang_vien('Nguyen Kim Hoang').
truong_bo_mon('Nguyen Kim Hoang','Thach hoc va Khoang san').
hoc_ham('Nguyen Kim Hoang','GVC').
hoc_vi('Nguyen Kim Hoang','TS').
nam('Nguyen Kim Hoang').



% Khoa Khoa hoc va Cong nghe vat lieu.
khoa('Khoa hoc va Cong nghe vat lieu').
truc_thuoc('Khoa hoc va Cong nghe vat lieu', 'DH KHTN').
bo_mon('Vat lieu Polymer va Composite').
bo_mon('Vat lieu Nano va Mang mong').
bo_mon('Vat lieu tu va Y sinh').
truc_thuoc('Vat lieu Polymer va Composite', 'Khoa khoa hoc va Cong nghe vat lieu').
truc_thuoc('Vat lieu Nano va Mang mong', 'Khoa khoa hoc va Cong nghe vat lieu').
truc_thuoc('Vat lieu tu va Y sinh', 'Khoa khoa hoc va Cong nghe vat lieu').

giang_vien('Tran Thi Thanh Van').
truong_khoa('Tran Thi Thanh Van','Khoa hoc va Cong nghe vat lieu').
hoc_ham('Tran Thi Thanh Van','PGS').
hoc_vi('Tran Thi Thanh Van','TS').
nu('Tran Thi Thanh Van').

giang_vien('Ha Thuc Chi Nhan').
pho_khoa('Ha Thuc Chi Nhan','Khoa hoc va Cong nghe vat lieu').
hoc_ham('Ha Thuc Chi Nhan','PGS').
hoc_vi('Ha Thuc Chi Nhan','TS').
nam('Ha Thuc Chi Nhan').

giang_vien('Tran Thi Minh Thu').
pho_khoa('Tran Thi Minh Thu','Khoa hoc va Cong nghe vat lieu').
hoc_vi('Tran Thi Minh Thu','ThS').
nu('Tran Thi Minh Thu').

giang_vien('Hoang Thi Dong Quy').
truong_bo_mon('Hoang Thi Dong Quy','Vat lieu Polymer va Composite').
hoc_ham('Hoang Thi Dong Quy','PGS').
hoc_vi('Hoang Thi Dong Quy','TS').
nu('Hoang Thi Dong Quy').

giang_vien('Pham Kim Ngoc').
truong_bo_mon('Pham Kim Ngoc','Vat lieu Nano va Mang mong').
hoc_vi('Pham Kim Ngoc','TS').
nu('Pham Kim Ngoc').

giang_vien('Le Van Hieu').
truong_bo_mon('Le Van Hieu','Vat lieu tu va Y sinh').
hoc_ham('Le Van Hieu','GS').
hoc_vi('Le Van Hieu','TS').
nam('Le Van Hieu').

giang_vien('Ta Thi Kieu Hanh').
pho_bo_mon('Ta Thi Kieu Hanh','Vat lieu tu va Y sinh').
hoc_vi('Ta Thi Kieu Hanh','ThS').
nu('Ta Thi Kieu Hanh').


% Khoa Moi truong.
khoa('Moi truong').
truc_thuoc('Moi truong', 'DH KHTN').
bo_mon('Khoa hoc Moi truong').
bo_mon('Cong nghe Moi truong').
bo_mon('Quan ly Moi truong').
bo_mon('Tin hoc Moi truong').

truc_thuoc('Khoa hoc Moi truong', 'Moi truong').
truc_thuoc('Cong nghe Moi truong', 'Moi truong').
truc_thuoc('Quan ly Moi truong', 'Moi truong').
truc_thuoc('Tin hoc Moi truong', 'Moi truong').

giang_vien('To Thi Hien').
truong_khoa('To Thi Hien','Moi truong').
truong_bo_mon('Thanh','Cong nghe Moi truong').
hoc_ham('To Thi Hien','PGS').
hoc_vi('To Thi Hien','TS').
nu('To Thi Hien').

giang_vien('Dao Nguyen Khoi').
pho_khoa('Dao Nguyen Khoi','Moi truong').
hoc_vi('Dao Nguyen Khoi','TS').
nam('Dao Nguyen Khoi').

giang_vien('Le Tu Thanh').
truong_bo_mon('Le Tu Thanh','Khoa hoc Moi truong').
hoc_vi('Le Tu Thanh','TS').
nam('Le Tu Thanh').

giang_vien('Truong Thi Cam Trang').
pho_bo_mon('Truong Thi Cam Trang','Cong nghe Moi truong').
hoc_vi('Truong Thi Cam Trang','TS').
nu('Truong Thi Cam Trang').

giang_vien('Nguyen Bich Ngoc').
truong_bo_mon('Nguyen Bich Ngoc','Quan ly Moi truong').
hoc_vi('Nguyen Bich Ngoc','TS').
nu('Nguyen Bich Ngoc').

giang_vien('Duong Thi Thuy Nga').
truong_bo_mon('Duong Thi Thuy Nga','Tin hoc Moi truong').
hoc_vi('Duong Thi Thuy Nga','TS').
nu('Duong Thi Thuy Nga').


% Dinh nghia cac vi tu.
giang_vien_thuoc_bo_mon(_giangVien, _boMon):-
    giang_vien(_giangVien),
    truc_thuoc(_giangVien, _boMon),
    bo_mon(_boMon).

giang_vien_thuoc_khoa(_giangVien, _khoa):-
    giang_vien(_giangVien),
    truc_thuoc(_giangVien, _boMon),
    bo_mon(_boMon),
    truc_thuoc(_boMon, _khoa),
    khoa(_khoa).

giang_vien_thuoc_truong(_giangVien, _truong):-
    giang_vien(_giangVien),
    truc_thuoc(_giangVien, _boMon),
    bo_mon(_boMon),
    truc_thuoc(_boMon, _khoa),
    khoa(_khoa),
    truc_thuoc(_khoa, _truong),
    truong(_truong).

bo_mon_thuoc_khoa(_boMon, _khoa):-
    bo_mon(_boMon),
    khoa(_khoa),
    truc_thuoc(_boMon, _khoa).

bo_mon_thuoc_truong(_boMon, _truong):-
    bo_mon(_boMon),
    truong(_truong),
    khoa(_khoa),
    truc_thuoc(_boMon, _khoa),
    truc_thuoc(_khoa, _truong).

khoa_thuoc_truong(_khoa, _truong):-
    khoa(_khoa),
    truong(_truong),
    truc_thuoc(_khoa, _truong).

truong_thuoc(_truong, _tochuc):-
    truong(_truong),
    to_chuc(_tochuc),
    truc_thuoc(_truong, _tochuc).

nganh_cung_khoa(_nganh01, _nganh02) :-
    \+ equal(_nganh01, _nganh02),
    nganh(_nganh01),
    nganh(_nganh02),
    truc_thuoc(_nganh01, _khoa01),
    truc_thuoc(_nganh02, _khoa02),
    khoa(_khoa01),
    khoa(_khoa02),
    equal(_khoa01, _khoa02).

chuyen_nganh_cung_nganh(_chuyenNganh01, _chuyenNganh02):-
    \+ equal(_chuyenNganh01, _chuyenNganh02),
    chuyen_nganh(_chuyenNganh01),
    chuyen_nganh(_chuyenNganh02),
    truc_thuoc(_chuyenNganh01, _nganh01),
    truc_thuoc(_chuyenNganh02, _nganh02),
    equal(_nganh01, _nganh02).

giang_vien_cung_bo_mon(_giangVien1, _giangVien2):-
    \+ equal(_giangVien1, _giangVien2),
    giang_vien(_giangVien1),
    giang_vien(_giangVien2),
    giang_vien_thuoc_bo_mon(_giangVien1, _boMon1),
    giang_vien_thuoc_bo_mon(_giangVien2, _boMon2),
    equal(_boMon1, _boMon2).

giang_vien_cung_khoa(_giangVien1, _giangVien2):-
    \+ equal(_giangVien1, _giangVien2),
    giang_vien(_giangVien1),
    giang_vien(_giangVien2),
    giang_vien_thuoc_khoa(_giangVien1, _khoa1),
    giang_vien_thuoc_khoa(_giangVien2, _khoa2),
    equal(_khoa1, _khoa2).

giang_vien_cung_truong(_giangVien1, _giangVien2):-
    \+ equal(_giangVien1, _giangVien2),
    giang_vien(_giangVien1),
    giang_vien(_giangVien2),
    giang_vien_thuoc_truong(_giangVien1, _truong1),
    giang_vien_thuoc_truong(_giangVien2, _truong2),
    equal(_truong1, _truong2).

bo_mon_cung_khoa(_boMon1, _boMon2):-
    \+ equal(_boMon1, _boMon2),
    bo_mon(_boMon1),
    bo_mon(_boMon2),
    bo_mon_thuoc_khoa(_boMon1, _khoa1),
    bo_mon_thuoc_khoa(_boMon2, _khoa2),
    equal(_khoa1, _khoa2).

giao_su_lam_truong_khoa(_giangVien):-
    giang_vien(_giangVien),
    hoc_ham(_giangVien, 'GS'),
    truong_khoa(_giangVien, _khoa),
    khoa(_khoa).

giao_su(_giangVien):-
    giang_vien(_giangVien),
    hoc_ham(_giangVien, 'GS').

pho_giao_su(_giangVien):-
    giang_vien(_giangVien),
    hoc_ham(_giangVien, 'PGS').

tien_si(_giangVien):-
    giang_vien(_giangVien),
    hoc_vi(_giangVien, 'TS').

thac_si(_giangVien):-
    giang_vien(_giangVien),
    hoc_vi(_giangVien, 'ThS').

giang_vien_chinh(_giangVien):-
    giang_vien(_giangVien),
    hoc_ham(_giangVien, 'GVC').

cung_la_giao_su(_giangVien01, _giangVien02):-
    giao_su(_giangVien01),
    giao_su(_giangVien02).

cung_la_pho_giao_su(_giangVien01, _giangVien02):-
    pho_giao_su(_giangVien01),
    pho_giao_su(_giangVien02).

cung_la_tien_si(_giangVien01, _giangVien02):-
    tien_si(_giangVien01),
    tien_si(_giangVien02).

cung_la_thac_si(_giangVien01, _giangVien02):-
    thac_si(_giangVien01),
    thac_si(_giangVien02).


vua_la_truong_khoa_vua_la_truong_bo_mon(_giangVien):-
    giang_vien(_giangVien),
    truong_bo_mon(_giangVien, _boMon),
    bo_mon(_boMon),
    bo_mon_thuoc_khoa(_boMon, _khoa),
    truong_khoa(_giangVien, _khoa).