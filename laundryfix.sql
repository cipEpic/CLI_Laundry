-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Jun 2022 pada 17.02
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laundrycoba`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id_admin`, `username`, `password`) VALUES
(1, 'admin2', 'admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `agen`
--

CREATE TABLE `agen` (
  `id_agen` int(11) NOT NULL,
  `nama_laundry` varchar(30) DEFAULT NULL,
  `nama_pemilik` varchar(30) DEFAULT NULL,
  `telp` varchar(13) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `kota` varchar(20) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `plat_driver` varchar(12) DEFAULT NULL,
  `foto` text NOT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `agen`
--

INSERT INTO `agen` (`id_agen`, `nama_laundry`, `nama_pemilik`, `telp`, `email`, `kota`, `alamat`, `plat_driver`, `foto`, `password`) VALUES
(1, 'laundry satu', 'pemilik1', '081231231231', 'laundry1@gmail.com', 'Klungkung', 'Jalan Krisna No. 3 Depan Banjar Papaan', 'DK 1215 NA', 'default.png', '$2y$10$4WXVd3Ly7TymaOHHJX2ZGeUe1/IwlcOY.xHzYhfIDSoCgpZAnTz1O'),
(2, 'laundry dua', 'pemilik2', '081223334444', 'laundry2@gmail.com', 'Denpasar', 'Jalan Danau Meninjau nomor 3', 'DK 1234 NA', 'default.png', '$2y$10$f4ERy2qulYfd/u32RVVbBu1/u.iigf1o6JI5SYi4c4ASBcgkYvcU2'),
(3, 'laundry tiga ', 'pemilik3', '081231098239', 'laundry3@gmail.com', 'Singaraja', 'Jalan Sudirman nomor 4', 'DK 1111 NA', 'default.png', '$2y$10$XU3iTzvUxd0Jah/X0GJJDOJ5lb1m6ZWZkdXyQY0scUZIxiSVygMgq'),
(4, 'laundry empat', 'pemilik4', '081231098239', 'laundry4@gmail.com', 'Karangasem', 'Jalan gunung agung nomor 3', 'DK 1246 NA', 'default.png', '$2y$10$x2QfNW9ftIR9dTACEfU.lOnwlw6793kB6Lw2Ru/29SNtz1HtoryRS');

-- --------------------------------------------------------

--
-- Struktur dari tabel `buangan`
--

CREATE TABLE `buangan` (
  `id_pelanggan` int(11) NOT NULL,
  `nama` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `telp` varchar(13) DEFAULT NULL,
  `kota` varchar(20) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `foto` text NOT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `cucian`
--

CREATE TABLE `cucian` (
  `id_cucian` int(11) NOT NULL,
  `id_agen` int(11) NOT NULL,
  `id_pelanggan` int(11) DEFAULT NULL,
  `tgl_mulai` date NOT NULL,
  `tgl_selesai` date NOT NULL,
  `jenis` varchar(15) DEFAULT NULL,
  `total_item` int(11) DEFAULT NULL,
  `berat` double DEFAULT NULL,
  `alamat` varchar(100) NOT NULL,
  `catatan` text NOT NULL,
  `status_cucian` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `cucian`
--

INSERT INTO `cucian` (`id_cucian`, `id_agen`, `id_pelanggan`, `tgl_mulai`, `tgl_selesai`, `jenis`, `total_item`, `berat`, `alamat`, `catatan`, `status_cucian`) VALUES
(10, 3, 3, '2022-06-14', '0000-00-00', 'komplit', 15, 3, 'Jalan muhammad yamin nomor 7, Singaraja', 'yang bersih ya', 'Sedang Di Jemur'),
(11, 1, 1, '2022-06-14', '0000-00-00', 'setrika', 5, 1, 'Jalan Krisna No. 3 Depan Banjar Papaan, Klungkung', 'yang rapi', 'Sedang di Setrika'),
(12, 1, 1, '2022-06-14', '0000-00-00', 'cuci', 10, 2, 'Jalan Krisna No. 3 Depan Banjar Papaan, Klungkung', '', 'Selesai'),
(13, 4, 2, '2022-06-14', '0000-00-00', 'komplit', 20, 4, 'Jalan gunung rinjani nomor 3, Karangasem', 'butuh cepat', 'Selesai');

-- --------------------------------------------------------

--
-- Struktur dari tabel `harga`
--

CREATE TABLE `harga` (
  `id_harga` int(11) NOT NULL,
  `jenis` varchar(30) NOT NULL,
  `id_agen` int(11) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `harga`
--

INSERT INTO `harga` (`id_harga`, `jenis`, `id_agen`, `harga`) VALUES
(1, 'cuci', 1, 4000),
(2, 'setrika', 1, 3000),
(3, 'komplit', 1, 6500),
(4, 'cuci', 2, 5500),
(5, 'setrika', 2, 4000),
(6, 'komplit', 2, 8000),
(7, 'cuci', 3, 3500),
(8, 'setrika', 3, 3500),
(9, 'komplit', 3, 6500),
(10, 'cuci', 4, 3000),
(11, 'setrika', 4, 2500),
(12, 'komplit', 4, 5000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id_pelanggan` int(11) NOT NULL,
  `nama` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `telp` varchar(13) DEFAULT NULL,
  `kota` varchar(20) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `foto` text NOT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pelanggan`
--

INSERT INTO `pelanggan` (`id_pelanggan`, `nama`, `email`, `telp`, `kota`, `alamat`, `foto`, `password`) VALUES
(1, 'pelanggan satu', 'pelanggan1@gmail.com', '085100343999', 'Klungkung', 'Jalan Krisna No. 3 Depan Banjar Papaan', 'default.png', '$2y$10$W.3WKW4K9WYhbreWJhJ4ouKse3HAFVFKAExvFtZJvEZzkO1Cpajne'),
(2, 'pelanggan dua', 'pelanggan2@gmail.com', '081232421968', 'Karangasem', 'Jalan gunung rinjani nomor 3', 'default.png', '$2y$10$pXyTCFJe.o/lxMwoDZy9MerzCD4k0hnflgnFDIluSL6EfPXkxLKza'),
(3, 'pelanggan tiga', 'pelanggan3@gmail.com', '088696966111', 'Singaraja', 'Jalan muhammad yamin nomor 7', 'default.png', '$2y$10$vEUMSoLpLtfYd.ztXsveSe/n3XqwzpH5nre2yJMGKGThcVZUG1jvK');

--
-- Trigger `pelanggan`
--
DELIMITER $$
CREATE TRIGGER `deleted_cucian` AFTER DELETE ON `pelanggan` FOR EACH ROW BEGIN
DELETE FROM cucian WHERE id_pelanggan = OLD.id_pelanggan;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `deleted_pelanggan` AFTER DELETE ON `pelanggan` FOR EACH ROW BEGIN
INSERT INTO buangan VALUES
(OLD.id_pelanggan, OLD.nama, OLD.email, OLD.telp, OLD.kota, OLD.alamat, OLD.foto, OLD.password);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `kode_transaksi` int(11) NOT NULL,
  `id_cucian` int(11) NOT NULL,
  `id_agen` int(11) NOT NULL,
  `id_pelanggan` int(11) NOT NULL,
  `tgl_mulai` date DEFAULT NULL,
  `tgl_selesai` date DEFAULT NULL,
  `total_bayar` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `komentar` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`kode_transaksi`, `id_cucian`, `id_agen`, `id_pelanggan`, `tgl_mulai`, `tgl_selesai`, `total_bayar`, `rating`, `komentar`) VALUES
(24, 12, 1, 1, '2022-06-14', '2022-06-14', 8000, 10, 'recommended'),
(25, 13, 4, 2, '2022-06-14', '2022-06-14', 20000, 8, 'mantap');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indeks untuk tabel `agen`
--
ALTER TABLE `agen`
  ADD PRIMARY KEY (`id_agen`);

--
-- Indeks untuk tabel `cucian`
--
ALTER TABLE `cucian`
  ADD PRIMARY KEY (`id_cucian`);

--
-- Indeks untuk tabel `harga`
--
ALTER TABLE `harga`
  ADD PRIMARY KEY (`id_harga`);

--
-- Indeks untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`kode_transaksi`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `agen`
--
ALTER TABLE `agen`
  MODIFY `id_agen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT untuk tabel `cucian`
--
ALTER TABLE `cucian`
  MODIFY `id_cucian` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT untuk tabel `harga`
--
ALTER TABLE `harga`
  MODIFY `id_harga` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `kode_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
