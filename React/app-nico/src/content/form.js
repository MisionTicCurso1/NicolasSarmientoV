import React from "react";
import {Router} from "@reach/router";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";

const validation= Yup.object().shape({
    nombs:Yup.string()
    .email('Invalid email')
    .required('The email is neccesary'),

    password:Yup.string()
    .min(8,'The minimum password lenght is 6 char')
    .required('The password is neccesary'),
});

export default function Form_login(){
    return(
        <Formik 
            initialValues={{nombs:'',password:''}}
            onSubmit={(values)=>{console.log(values)}}
            validationSchema={validation}
        >
            {(props)=>(
                <Form>
                    <label>E-mail</label>
                    <Field type='email' name='nombs' placeholder='Your email'/>
                    <ErrorMessage name='nombs' component='div'/>

                    <label>password</label>
                    <Field type='password' name='password' placeholder='Your password'/>
                    <ErrorMessage name='password' component='div'/>

                    <button type='submit'>Enviar</button>
                   
                </Form>
            )}
        </Formik>
    );
}