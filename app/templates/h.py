{% for x in job_title%}
    <a href="{%url "jobs_detail" x.id %}"> <h3>{{x}}</h3></a>
{% endfor 
