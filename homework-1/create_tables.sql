BEGIN;


CREATE TABLE IF NOT EXISTS public.customers
(
    customer_id character varying(5) COLLATE pg_catalog."default" NOT NULL,
    company_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    contact_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT customers_pkey PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS public.employees
(
    employee_id integer NOT NULL DEFAULT nextval('employees_employee_id_seq'::regclass),
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    title character varying(50) COLLATE pg_catalog."default" NOT NULL,
    birth_date date NOT NULL,
    notes text COLLATE pg_catalog."default",
    CONSTRAINT employees_pkey PRIMARY KEY (employee_id)
);

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer NOT NULL DEFAULT nextval('orders_order_id_seq'::regclass),
    customer_id character varying(5) COLLATE pg_catalog."default" NOT NULL,
    employee_id integer NOT NULL,
    order_date date NOT NULL,
    ship_city character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT orders_pkey PRIMARY KEY (order_id)
);

ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id)
    REFERENCES public.customers (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT orders_employee_id_fkey FOREIGN KEY (employee_id)
    REFERENCES public.employees (employee_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;