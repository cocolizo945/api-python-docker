-- Creacion de tablas
CREATE TABLE IF NOT EXISTS general_task.admin_task
(
    id_task bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name_task "char"[] NOT NULL,
    admin_id bigint NOT NULL,
    template_id bigint NOT NULL,
    start_range time with time zone,
    end_range time with time zone,
    status integer DEFAULT 1,
    description "char",
    repeat_task boolean,
    initial_date date,
    end_date date,
    level_task integer,
    CONSTRAINT admin_task_pkey PRIMARY KEY (id_task)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS general_task.admin_task
    OWNER to postgres;
--###################################################################
CREATE TABLE IF NOT EXISTS general_task.canceled_task
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_task bigint NOT NULL,
    user_id bigint NOT NULL,
    description character varying(150) COLLATE pg_catalog."default",
    time_cancel timestamp with time zone,
    number_pics integer,
    CONSTRAINT canceled_task_pkey PRIMARY KEY (id_task),
    CONSTRAINT id_task_cancel FOREIGN KEY (id_task)
        REFERENCES general_task.admin_task (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS general_task.canceled_task
    OWNER to postgres;
--###################################################################
CREATE TABLE IF NOT EXISTS general_task.photo_task
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_task bigint NOT NULL,
    date_time timestamp with time zone,
    path_photo path,
    CONSTRAINT photo_task_pkey PRIMARY KEY (id_task),
    CONSTRAINT id_task_photo FOREIGN KEY (id_task)
        REFERENCES general_task.admin_task (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS general_task.photo_task
    OWNER to postgres;
--###################################################################
CREATE TABLE IF NOT EXISTS general_task.status
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    description character(50) COLLATE pg_catalog."default",
    CONSTRAINT status_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS general_task.status
    OWNER to postgres;
--###################################################################
CREATE TABLE IF NOT EXISTS general_task.user_task
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_task bigint NOT NULL,
    user_id bigint NOT NULL,
    template_id bigint,
    start_time time with time zone,
    end_time time with time zone,
    observations "char",
    CONSTRAINT user_task_pkey PRIMARY KEY (id),
    CONSTRAINT id_task_constrain FOREIGN KEY (id_task)
        REFERENCES general_task.admin_task (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS general_task.user_task
    OWNER to postgres;
--###################################################################
-- insercion de data a tabla status
insert into general_task.status values (default,'Por Iniciar');
insert into general_task.status values (default,'En Proceso');
insert into general_task.status values (default,'En Pausa');
insert into general_task.status values (default,'No Realizado');
insert into general_task.status values (default,'Cancelado');
--###################################################################

ALTER TABLE general_task.admin_task
    ALTER COLUMN name_task TYPE text;

--######################################################################
DROP FUNCTION photo_insert(_id bigint, _id_task bigint, _date_time timestamp with time zone, _path_photos path)

RETURN bigint
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO photo_task(id, id_task,)
-------------------

CREATE OR REPLACE FUNCTION general_task.insert_user(IN p_name text,IN p_second_name text,IN p_cellphone bigint,IN p_password text)
    RETURNS bigint
    LANGUAGE 'plpgsql'
    VOLATILE
    PARALLEL UNSAFE
    COST 100
    
AS $BODY$
DECLARE
BEGIN
    EXECUTE 'INSERT INTO general_task.users (name, second_name, cellphone, password)
    VALUES ('''||p_name||''', '''||p_second_name||''', '''||p_cellphone||''', '''||p_password||''')';
	RETURN 200;
exception 
	when others then 
	return 400;
END;
$BODY$;

--------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION general_task.update_user(IN p_id bigint,IN p_name text,IN p_second_name text,IN p_cellphone bigint,IN p_password text)
    RETURNS bigint
    LANGUAGE 'plpgsql'
    VOLATILE
    PARALLEL UNSAFE
    COST 100
    
AS $BODY$
DECLARE
BEGIN
    EXECUTE 'UPDATE general_task.users SET  
	name = '''||p_name||''',
	second_name = '''||p_second_name||''',
	cellphone = '''||p_cellphone||''',
	password = '''||p_password||'''
	WHERE id = '''||p_id||'''';
    	RETURN 200;
exception
	when others then
	return 400;
END;
$BODY$;