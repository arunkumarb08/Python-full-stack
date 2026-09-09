import React, { useEffect, useState } from 'react'

function Products() {
    const [products, setProducts] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch('https://fakestoreapi.com/products')
            .then((res) => res.json())
            .then((data) => {
                setProducts(data);
                setLoading(false)
            })
            .catch((err) => console.log(err));
    }, [])

    if (loading) return <p>loading...</p>
    return (
        <div>
            <h1 style={{ textAlign: "center", paddingTop: "20px" }}>---New Arrivals---</h1>
            <div style={styles.grid}>
                {products.map(product => (
                    <div key={product.id} style={styles.card}>
                        <img src={product.image} style={styles.img} />
                        <h4>{product.title}</h4>
                        <p>${product.price}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}
const styles = {
    grid: {
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit,minmax(200px, 1fr))",
        gap: "20px",
        padding: "40px",
    },
    card: {
        border: "1px solid #dddd",
        borderRadius: "5px",
        padding: "15px",
        textAlign: "center",
    },
    img: {
        width: "140px",
        height: "150px",
        objectFit: "contain",
    },
}

export default Products