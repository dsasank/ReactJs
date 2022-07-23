import React, { useEffect, useState } from 'react'
import jd from "./MOCK_DATA.js"

const Audio=()=>{
    const [data,setData]=useState([])
    useEffect(()=>{
        fakestore()
    },[])
    const [bef,setBef]=useState("")
    const fakestore=async()=>{
        const fakedata=await fetch("https://fakestoreapi.com/products")
        const findata=await fakedata.json()
        console.log(findata)
        setData(findata)
    }

     
        return(

        
            <>   
            <input type="text" onChange={(e)=>{setBef(e.target.value)}} ></input>
            {console.log(bef)}
            
            {data.filter((value)=>{if(value.title.includes(bef)){return value}}).map((value)=>{
                return(
                    <>
                    <h1>{value.title}</h1>
                    </>
                )

            })}
           
  
            </>
        )
}
export default Audio