<div><strong>C</strong>reate 
    <strong>R</strong>ead 
    <strong>U</strong>pdate
    <strong>D</strong>elete</div>
<h2>{{ name }}</h2>
<form action="/crud" method="POST">
% for name in sorted(form._fields):
<div>
% field = getattr(form, name)
% field
{{ name }} 
</div>
% end
</form>
%rebase base
