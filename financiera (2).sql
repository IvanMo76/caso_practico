-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-07-2026 a las 07:55:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `financiera`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_admin`
--

CREATE TABLE `tbl_admin` (
  `id_admin` int(11) NOT NULL,
  `nombre_admin` varchar(50) NOT NULL,
  `ap_admin` varchar(50) NOT NULL,
  `am_admin` varchar(50) DEFAULT NULL,
  `correo` varchar(100) NOT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `psw` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_admin`
--

INSERT INTO `tbl_admin` (`id_admin`, `nombre_admin`, `ap_admin`, `am_admin`, `correo`, `imagen`, `psw`) VALUES
(1, 'Juan', 'Pérez', 'García', 'juan@financiera.com', 'https://randomuser.me/api/portraits/men/1.jpg', '123456789'),
(2, 'María', 'López', 'Martínez', 'maria@financiera.com', 'https://randomuser.me/api/portraits/women/2.jpg', '123456789'),
(3, 'Carlos', 'Hernández', 'Ruiz', 'carlos@financiera.com', 'https://randomuser.me/api/portraits/men/3.jpg', '123456789'),
(4, 'Ana', 'Morales', 'Sánchez', 'ana@financiera.com', 'https://randomuser.me/api/portraits/women/4.jpg', '123456789');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_cards`
--

CREATE TABLE `tbl_cards` (
  `id_card` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_cards`
--

INSERT INTO `tbl_cards` (`id_card`, `titulo`, `descripcion`, `imagen`) VALUES
(1, 'Crédito Automotriz', 'Financiamiento para automóviles seminuevos.', 'https://images.unsplash.com/photo-1503376780353-7e6692767b70'),
(2, 'Crédito Personal', 'Préstamos personales con rápida aprobación.', 'https://images.unsplash.com/photo-1554224155-6726b3ff858f'),
(3, 'Financiamiento para Motocicletas', 'Planes accesibles para motocicletas.', 'https://images.unsplash.com/photo-1558981806-ec527fa84c39'),
(4, 'Tasas Competitivas', 'Las mejores tasas del mercado.', 'https://images.unsplash.com/photo-1520607162513-77705c0f0d4a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_carrusel`
--

CREATE TABLE `tbl_carrusel` (
  `id_imagen` int(11) NOT NULL,
  `imagen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_carrusel`
--

INSERT INTO `tbl_carrusel` (`id_imagen`, `imagen`) VALUES
(7, 'exec-37405749-e244-4cf6-9d89-0a4be5f428b3.png'),
(8, 'credito.png'),
(9, 'productos.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_catal_autos`
--

CREATE TABLE `tbl_catal_autos` (
  `id_auto` int(11) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `anio` varchar(80) NOT NULL,
  `km` int(11) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `descripcion` mediumtext NOT NULL,
  `precio_unidad` int(11) NOT NULL,
  `imagen` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_catal_autos`
--

INSERT INTO `tbl_catal_autos` (`id_auto`, `modelo`, `anio`, `km`, `marca`, `tipo`, `descripcion`, `precio_unidad`, `imagen`) VALUES
(1, 'Fenix', '2022', 45000, 'Falcora', 'suv', 'pickup todo terreno', 50000, 'f150_1.jpg'),
(2, 'Nebula', '2021', 42000, 'Astera Motors', 'suv', 'Vehículo familiar en excelentes condiciones.', 220000, 'descarga_1.jpg'),
(3, 'Elion', '2023', 18000, 'Solvian', 'sedan', 'Transmisión automática.', 350000, 'jetta.jpg'),
(4, 'Atria', '2022', 25000, 'Novaris', 'sedan', 'Seminuevo con servicios de agencia.', 320000, 'descarga_2.jpg'),
(5, 'Celsa', '2015', 12000, 'Astera Motors', 'pickup', 'fssdgdsg', 34325345, 'descarga.jpg'),
(7, 'Vectora', '2018', 0, 'Novaris', 'pickup', 'La Ford F-250 es una camioneta de trabajo pesado diseñada para ofrecer un excelente equilibrio entre potencia, resistencia y confort. Su diseño robusto y moderno proyecta una presencia imponente, mientras que su amplio espacio interior y tecnología integrada brindan una experiencia de conducción cómoda tanto para el trabajo como para el uso diario.\r\n\r\nEquipada con un motor de alto rendimiento, la F-250 destaca por su capacidad de carga y arrastre, convirtiéndose en una opción ideal para actividades comerciales, agrícolas, de construcción o para quienes requieren un vehículo confiable para transportar equipo y remolques. Su suspensión reforzada y su estructura de alta resistencia garantizan estabilidad y seguridad incluso en las condiciones más exigentes.\r\n\r\nEn el interior, ofrece una cabina espaciosa con acabados de calidad, sistema de infoentretenimiento con pantalla táctil, conectividad para dispositivos móviles, controles intuitivos y múltiples compartimentos de almacenamiento que aumentan la comodidad de todos los ocupantes.\r\n\r\n### Características destacadas\r\n\r\n* Motor de alto desempeño.\r\n* Excelente capacidad de carga y remolque.\r\n* Cabina amplia y confortable.\r\n* Sistema multimedia con pantalla táctil.\r\n* Aire acondicionado y controles ergonómicos.\r\n* Dirección asistida y sistemas avanzados de seguridad.\r\n* Ideal para trabajo, uso empresarial y actividades todoterreno.\r\n\r\nLa **Ford F-250** representa una combinación de fuerza, tecnología y confiabilidad, siendo una de las mejores alternativas para quienes buscan una camioneta preparada para afrontar cualquier desafío sin sacrificar comodidad y estilo.\r\n', 50000, 'f250-motor.png,f250-interior.png,f250-3.png,f250-2.png,f250-1.png'),
(8, 'Forten', '2026', 0, 'Kronvia', 'sedan', 'dfksfksdnlksnfkls', 500000, 'fondo_login.png'),
(9, 'Kyra', '2026', 0, 'Zentari', 'sedan', 'El Chevrolet Onix es un sedán subcompacto (segmento B) destacado por su motorización turbo eficiente y gran nivel de conectividad. Equipado principalmente con un motor 1.0 L turbo de 3 cilindros (114 HP), destaca por su excelente rendimiento de combustible, amplio espacio en cajuela (470 litros) y 6 bolsas de aire de', 300000, 'f250-3.png'),
(10, 'Vela', '2025', 1200, 'Astera Motors', 'sedan', 'Auto prueba', 566777, 'f250-1.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_coti_auto`
--

CREATE TABLE `tbl_coti_auto` (
  `id_coti_auto` int(11) NOT NULL,
  `id_auto` int(11) NOT NULL,
  `nombre_cliente` varchar(50) NOT NULL,
  `ap_cliente` varchar(50) NOT NULL,
  `am_cliente` varchar(50) DEFAULT NULL,
  `celular_cliente` varchar(15) DEFAULT NULL,
  `correo_cliente` varchar(100) DEFAULT NULL,
  `fecha_coti` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_coti_auto`
--

INSERT INTO `tbl_coti_auto` (`id_coti_auto`, `id_auto`, `nombre_cliente`, `ap_cliente`, `am_cliente`, `celular_cliente`, `correo_cliente`, `fecha_coti`) VALUES
(1, 1, 'Pedro', 'Ramírez', 'Luna', '2147483647', 'pedro@gmail.com', '2026-05-01 10:30:00'),
(2, 2, 'Luis', 'Gómez', 'Díaz', '2147483647', 'luis@gmail.com', '2026-05-03 12:15:00'),
(3, 3, 'José', 'Torres', 'Hernández', '2147483647', 'jose@gmail.com', '2026-05-05 15:40:00'),
(4, 4, 'Miguel', 'Vargas', 'Flores', '2147483647', 'miguel@gmail.com', '2026-05-08 09:20:00'),
(13, 2, 'Ivan', 'Ivan', 'Moreno', '2147483647', 'ivanmorenodej@gmail.com', '2026-07-08 17:22:42'),
(14, 2, 'Ivan', 'Ivan', 'Moreno', '2147483647', 'ivanmorenodej@gmail.com', '2026-07-08 17:23:23'),
(16, 2, 'Rosendo', 'Moreno', 'Cruz', '6536364262', 'ros1276@gmail.com', '2026-07-08 23:37:50'),
(17, 1, 'Ivan', 'Moreno ', 'De jesus', '1276145071', 'ivanmorenodej@gmail.com', '2026-07-09 10:25:04'),
(18, 1, 'Rosendo', 'Moreno ', 'De jesus', '9793279075', 'rosendo@gmail.com', '2026-07-09 18:23:17'),
(19, 7, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-09 19:01:35'),
(20, 7, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-09 19:01:45'),
(21, 5, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-09 19:03:00'),
(22, 8, 'Edgar', 'Perez ', 'Lopez', '3989834623', 'edg1276@gmail.com', '2026-07-09 21:43:12'),
(24, 2, 'Rosendo', 'Moreno', 'Cruz', '7122529507', 'rosendo1276@gmail.com', '2026-07-14 12:38:12'),
(25, 4, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-14 13:01:38'),
(26, 9, 'Juan', 'perez', 'Hernandez', '9812648961', 'hernandez1276@gmail.com', '2026-07-14 14:26:26'),
(27, 2, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-17 18:51:29'),
(28, 2, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-17 18:52:57'),
(29, 7, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', '2026-07-17 19:44:26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_credito`
--

CREATE TABLE `tbl_credito` (
  `id_credito` int(11) NOT NULL,
  `nombre_cliente` varchar(50) NOT NULL,
  `ap_cliente` varchar(50) NOT NULL,
  `am_cliente` varchar(50) DEFAULT NULL,
  `celular_cliente` varchar(15) DEFAULT NULL,
  `correo_cliente` varchar(100) DEFAULT NULL,
  `monto` decimal(12,2) NOT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_credito`
--

INSERT INTO `tbl_credito` (`id_credito`, `nombre_cliente`, `ap_cliente`, `am_cliente`, `celular_cliente`, `correo_cliente`, `monto`, `fecha`) VALUES
(2, 'Patricia', 'Mendoza', 'López', '7122222222', 'patricia@gmail.com', 200000.00, '2026-05-04 14:30:00'),
(3, 'Ricardo', 'Nava', 'Martínez', '7123333333', 'ricardo@gmail.com', 180000.00, '2026-05-06 16:45:00'),
(5, 'Luis', 'Ramirez', 'Lopez', '7129876543', 'luis@gmail.com', 150000.00, '2026-05-29 22:34:04'),
(6, 'Ivan', 'Moreno', 'De jesus', '7122529506', 'ivanmorenodej@gmail.com', 50000.00, '2026-07-06 22:16:56'),
(7, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 600000.00, '2026-07-09 12:26:25'),
(9, 'Ivan', 'Moreno', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 70000.00, '2026-07-10 00:00:10'),
(12, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 50000.00, '2026-07-14 13:02:25'),
(13, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 70000.00, '2026-07-14 13:02:37'),
(14, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 100000.00, '2026-07-14 14:07:33'),
(15, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 60000.00, '2026-07-17 18:19:09'),
(16, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 50000.00, '2026-07-17 18:23:10'),
(17, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 567868678.00, '2026-07-17 18:27:38'),
(18, 'Ivan', 'Ivan', 'Moreno', '7122529506', 'ivanmorenodej@gmail.com', 50000.00, '2026-07-17 18:44:37');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `tbl_cards`
--
ALTER TABLE `tbl_cards`
  ADD PRIMARY KEY (`id_card`);

--
-- Indices de la tabla `tbl_carrusel`
--
ALTER TABLE `tbl_carrusel`
  ADD PRIMARY KEY (`id_imagen`);

--
-- Indices de la tabla `tbl_catal_autos`
--
ALTER TABLE `tbl_catal_autos`
  ADD PRIMARY KEY (`id_auto`);

--
-- Indices de la tabla `tbl_coti_auto`
--
ALTER TABLE `tbl_coti_auto`
  ADD PRIMARY KEY (`id_coti_auto`),
  ADD KEY `fk_coti_auto` (`id_auto`);

--
-- Indices de la tabla `tbl_credito`
--
ALTER TABLE `tbl_credito`
  ADD PRIMARY KEY (`id_credito`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tbl_cards`
--
ALTER TABLE `tbl_cards`
  MODIFY `id_card` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tbl_carrusel`
--
ALTER TABLE `tbl_carrusel`
  MODIFY `id_imagen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tbl_catal_autos`
--
ALTER TABLE `tbl_catal_autos`
  MODIFY `id_auto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `tbl_coti_auto`
--
ALTER TABLE `tbl_coti_auto`
  MODIFY `id_coti_auto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `tbl_credito`
--
ALTER TABLE `tbl_credito`
  MODIFY `id_credito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_coti_auto`
--
ALTER TABLE `tbl_coti_auto`
  ADD CONSTRAINT `fk_coti_auto` FOREIGN KEY (`id_auto`) REFERENCES `tbl_catal_autos` (`id_auto`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
