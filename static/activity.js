const postBox = document.getElementById('post-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBox = document.getElementById('loading-box')
const loadBtn = document.getElementById('load-btn')

let visible = 3

const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/post-json-view/${visible}/`,
        success: function (response) {
            max_size = response.max
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                data.map(post => {

                    postBox.innerHTML += `<div style="text-align: center" class="card p-3 mt-3 mb-3">

                                                ${post.activity_name}
                                               <br>
                                               ${post.active}
                                               <br>
                                               ${post.address}
                                               <br>
                                               ${post.description}
                                            </div>`
                })
                if (max_size) {
                    loadBox.innerHTML = "<h3>No More post lo load</h3>"

                }
            }, 500)
        },
        error: function (error) {
            console.log(error)
        }
    })
}


handleGetData()

loadBtn.addEventListener('click', () => {
    visible += 3
    handleGetData()
})