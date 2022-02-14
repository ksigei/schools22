function showMore() {
var modal = document.getElementById('blog');
modal.innerHTML += `
    <article>
        <figure>
         <img src="{{ post.image.url }}" class="rounded" alt="{{post.title}}">
        </figure>
        <div class="mt-3">
            <h1>${post.title}</h1>
            <p class="text-muted">
                Published {{ post.publish.date }} by <strong>{{ post.author }}</strong>
            </p>
        </div>

        <div class="article-body">
            {{post.body|safe}}
        </div>
        
    </article>
    
                                                               
`
}

