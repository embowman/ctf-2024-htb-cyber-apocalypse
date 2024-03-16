async function CheckMessage() {
    await fetch("", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'command': "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack" })
    })
    .then((res) => res.json())
    .then(async (data) => {
        console.log(data)
    })
}

CheckMessage()