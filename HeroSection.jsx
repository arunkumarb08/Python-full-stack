import React from 'react'

function HeroSection() {
  return (
    <section style={styles.hero}>
      <div style={styles.overlay}>
        <h1 style={styles.heading}>Welcome to Fake Store</h1>
        <p style={styles.paragraph}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus beatae quia veritatis! Facere rem numquam necessitatibus totam, molestias laboriosam cum unde sit eius natus pariatur! Culpa officiis unde aspernatur iure.</p>
        <button style={styles.button}>Shop Now</button>
      </div>
    </section>
  )
}

const styles = {
  hero: {
    backgroundImage: "url('/src/assets/black-friday-sales-sign-neon-light.jpg')",
    width: "100%",
    height: "100vh",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    display: "flex",
    alignItems: "Center",
    justifyContent: "center",
  },
  overlay: {
    width: "100%",
    height: "100%",
    display: "flex",
    justifyContent: "center",
    flexDirection: "column",
    alignItems: "center",
    // backgroundColor: "rgb",
  },
  heading: {
    color: "white",
    fontSize: "4rem",
  },
  paragraph: {
    color: "yellow",
    fontSize: "1rem",
    padding: "0 200px",
    textAlign: "center",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "black",
    color: "white",
    border: "none",
    borderRadius: "50px",
    marginTop: '20px',
    fontSize: "15px",
  }
}

export default HeroSection