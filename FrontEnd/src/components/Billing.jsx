import React from 'react'
import {  aibot } from '../assets'
import styles, { layout } from '../style'

const Billing = () => {
  return (
    <section id='product' className={layout.sectionReverse}>
      <div className={layout.sectionImgReverse}>
        <img
          src={aibot}
          alt='billing'
          className='w-[100%] h-[100%] relative z-[5]'
        />
        <div className='absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient'/>
        <div className='absolute z-[0] -left-1/2 bottom-0 w-[50%] h-[50%] rounded-full pink__gradient'/>
      </div>
      <div className={layout.sectionInfo}>
        <h2 className={styles.heading2}>Easily gain the  knowledge  <br className='sm:block hidden'/> using our legal ai assistant.</h2>
        <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
          Gain knowledge about diffrent laws and acts with this ai assistant.
        </p>
        <div className='flex flex-row flex-wrap sm:mt-10 mt-6'>
          
        </div>
      </div>  
    </section>
  )
}

export default Billing
