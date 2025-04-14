CREATE TABLE preguntas(
    id SERIAL PRIMARY KEY,
    pregunta TEXT NOT NULL,
    alternativas TEXT[] NOT NULL,
    respuesta_correcta TEXT NOT NULL ,
    nivel TEXT NOT NULL CHECK(nivel IN ('facil','intermedio','dificil'))
);


INSERT INTO preguntas (pregunta, alternativas, respuesta_correcta, nivel) VALUES
('¿Cuál es la capital de España?', ARRAY['Madrid', 'Barcelona', 'Valencia', 'Sevilla'], 'Madrid', 'facil'),
('¿Cuánto es 2 + 2?', ARRAY['3', '4', '5', '6'], '4', 'facil'),
('¿De qué color es el cielo en un día despejado?', ARRAY['Azul', 'Rojo', 'Verde', 'Gris'], 'Azul', 'facil'),
('¿Qué animal dice “miau”?', ARRAY['Perro', 'Gato', 'Pájaro', 'Vaca'], 'Gato', 'facil'),
('¿Cuál es el idioma oficial de Perú?', ARRAY['Quechua', 'Español', 'Portugués', 'Inglés'], 'Español', 'facil'),
('¿Qué fruta es amarilla y curva?', ARRAY['Manzana', 'Banana', 'Pera', 'Sandía'], 'Banana', 'facil'),
('¿Cuántos días tiene una semana?', ARRAY['5', '6', '7', '8'], '7', 'facil'),
('¿Qué planeta es conocido como el planeta rojo?', ARRAY['Marte', 'Júpiter', 'Venus', 'Saturno'], 'Marte', 'facil'),
('¿Qué instrumento tiene teclas blancas y negras?', ARRAY['Guitarra', 'Violín', 'Piano', 'Flauta'], 'Piano', 'facil'),
('¿Qué líquido bebemos más comúnmente?', ARRAY['Leche', 'Refresco', 'Agua', 'Jugo'], 'Agua', 'facil');


INSERT INTO preguntas (pregunta, alternativas, respuesta_correcta, nivel) VALUES
('¿Quién pintó La Mona Lisa?', ARRAY['Picasso', 'Da Vinci', 'Van Gogh', 'Rembrandt'], 'Da Vinci', 'intermedio'),
('¿En qué continente está Egipto?', ARRAY['Asia', 'Europa', 'África', 'Oceanía'], 'África', 'intermedio'),
('¿Cuál es el símbolo químico del oro?', ARRAY['Au', 'Ag', 'Fe', 'Hg'], 'Au', 'intermedio'),
('¿Cuál es el resultado de 12 x 8?', ARRAY['96', '88', '108', '100'], '96', 'intermedio'),
('¿Quién escribió "Cien años de soledad"?', ARRAY['Pablo Neruda', 'Mario Vargas Llosa', 'Gabriel García Márquez', 'Isabel Allende'], 'Gabriel García Márquez', 'intermedio'),
('¿Qué país tiene forma de bota?', ARRAY['Brasil', 'Italia', 'India', 'Grecia'], 'Italia', 'intermedio'),
('¿Qué gas respiramos para vivir?', ARRAY['Oxígeno', 'Nitrógeno', 'Dióxido de carbono', 'Hidrógeno'], 'Oxígeno', 'intermedio'),
('¿Qué órgano del cuerpo humano bombea sangre?', ARRAY['Hígado', 'Pulmón', 'Cerebro', 'Corazón'], 'Corazón', 'intermedio'),
('¿Cuál es el océano más grande del mundo?', ARRAY['Atlántico', 'Índico', 'Ártico', 'Pacífico'], 'Pacífico', 'intermedio'),
('¿Qué país inventó la pólvora?', ARRAY['Japón', 'India', 'China', 'Egipto'], 'China', 'intermedio');


INSERT INTO preguntas (pregunta, alternativas, respuesta_correcta, nivel) VALUES
('¿En qué año cayó el Imperio Romano de Occidente?', ARRAY['476 d.C.', '1453', '1492', '800 d.C.'], '476 d.C.', 'dificil'),
('¿Cuál es la capital de Mongolia?', ARRAY['Ulan Bator', 'Tashkent', 'Bishkek', 'Astana'], 'Ulan Bator', 'dificil'),
('¿Quién desarrolló la teoría de la relatividad?', ARRAY['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Nikola Tesla'], 'Albert Einstein', 'dificil'),
('¿Cuál es el río más largo del mundo según estudios recientes?', ARRAY['Nilo', 'Amazonas', 'Yangtsé', 'Misisipi'], 'Amazonas', 'dificil'),
('¿Cuál es el número atómico del Oxígeno?', ARRAY['6', '8', '10', '16'], '8', 'dificil'),
('¿Qué filósofo escribió "La República"?', ARRAY['Platón', 'Sócrates', 'Aristóteles', 'Epicuro'], 'Platón', 'dificil'),
('¿Qué país no pertenece a la Unión Europea?', ARRAY['Noruega', 'España', 'Francia', 'Italia'], 'Noruega', 'dificil'),
('¿Qué unidad se usa para medir la intensidad de la corriente eléctrica?', ARRAY['Voltio', 'Ohmio', 'Amperio', 'Watt'], 'Amperio', 'dificil'),
('¿Qué novela fue escrita por Mary Shelley?', ARRAY['Drácula', 'Frankenstein', 'El extraño caso de Dr. Jekyll y Mr. Hyde', 'El retrato de Dorian Gray'], 'Frankenstein', 'dificil'),
('¿Qué científico propuso las leyes del movimiento y la gravitación universal?', ARRAY['Newton', 'Kepler', 'Einstein', 'Galileo'], 'Newton', 'dificil');

