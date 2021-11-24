import styled, {css, keyframes} from "styled-components"

const fadeIn = ({time= "1s", type= "ease"} = {}) =>
    css`
        animation: ${time} ${fadeInkeyframe} ${type};`;


const fadeInkeyframe = keyframes `
    from{
        filter: blur(5px);
        opacity: 0
    }
    to{
        filter: blur(0);
        opacity: 1
    }
`


export const ImgWrapper = styled.div`
    border-radius: 10px;
    width: 200px;
    height: 200px;
    overflow: hidden;
    /* padding: 56% 0 0 0 ; */
    position: relative;


`

export const Img = styled.img`
    ${fadeIn({time: "1s"})}
    box-shadow: 0 10px 14px rgba(0,0,0,0.2);
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    width: 100%;
`


export const InfProd = styled.a`
    display: flex;
    flex-direction: column;
    text-align: center;
    text-decoration: none;
    width: 75px;

`

export const ImgProd = styled.img`
   border: 1px solid #ddd;
   box-shadow: 0px 10px 14px rgba(0,0,0, .2);
   border-radius: 50%;
   height: 75px;
   width: 75px;
   overflow: hidden;
   object-fit: cover;`

export const List = styled.ul`
  display: flex;
  overflow: scroll;
  width: 100%;
  padding: 1.3rem;
  ${(props) =>
    props.fixed &&
    css`
      background: #fff;
      border-radius: 60px;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
      left: 0;
      margin: 0 auto;
      max-width: 400px;
      padding: 5px;
      position: fixed;
      right: 0;
      top: -20px;
      transform: scale(0.5);
      z-index: 1;
    `}/* &.fixed {
   
  } */
`;

export const ItemList = styled.li`
  padding: 0 8px;
  font-size: 0.9vw;
  @media (max-width: 800px) {
    font-size: 1.9vw;
    color: blue;
  }
  @media only screen and (min-width: 1100px) and (max-width: 1350px) {
    font-size: 1.3vw;
    color: green;
  }
  @media only screen and (min-width: 768px) and (max-width: 1100px) {
    font-size: 1.45vw;
    color: green;
  }
  @media only screen and (min-width: 480px) and (max-width: 768px) {
    font-size: 1.9vw;
    color: yellow;
  }
`;