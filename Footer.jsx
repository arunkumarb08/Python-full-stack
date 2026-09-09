import React from 'react'

function Footer() {
    return (
        <footer style={styles.footer}>
            <p> &copy; CopyRights Reserved </p>
        </footer>
    )
}

const styles = {
    footer: {
        background: "black",
        color: "white",
        padding: "20px",
        textAlign: "center",

    }
}

export default Footer