?- giang_vien('Nguyen Dinh Thuc').
?- bo_mon_cung_khoa('Khoa hoc may tinh', BoMon).
?- tien_si('Le Ngoc Thanh').
?- giao_su('Le Hoai Bac').
?- nganh(_nganh), truc_thuoc(_nganh, 'CNTT').
?- chuyen_nganh(_chuyen_nganh), truc_thuoc(_chuyen_nganh,_nganh), truc_thuoc(_nganh, 'CNTT').
?- nam_thanh_lap('CNTT', _year).
?- truong_khoa('Dinh Ba Tien', 'CNTT').
?- pho_khoa(_phoKhoa, 'CNTT').
?- giao_su(_giaosu), truc_thuoc(_giaosu, _nganh), truc_thuoc(_nganh, 'CNTT').
?- pho_giao_su(_phogiaosu), truc_thuoc(_phogiaosu, _nganh), truc_thuoc(_nganh, 'CNTT').
?- tien_si(_giangvien), truc_thuoc(_giangvien, _nganh), truc_thuoc(_nganh, 'CNTT').
?- thac_si(_giangvien), truc_thuoc(_giangvien, _nganh), truc_thuoc(_nganh, 'CNTT').
?- nganh_cung_khoa('Khoa hoc may tinh', 'Ky thuat phan mem').
?- cung_la_giao_su('Le Hoai Bac', 'Ly Quoc Ngoc').
?- khoa(_khoa), truc_thuoc(_khoa, 'DH KHTN').
?- truong_bo_mon(_truongBoMonKHMT, 'Khoa hoc may tinh').
?- pho_bo_mon(_phoTruongBoMonKHMT, 'Khoa hoc may tinh').
?- giao_su('Le Nhut Nam').
?- chuyen_nganh_cung_nganh('Cong nghe tri thuc', 'Thi giac may tinh va dieu khien hoc thong minh').
?- equal(X, X).




