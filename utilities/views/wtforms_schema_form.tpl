<div class="container">
 <div><strong>C</strong>reate 
      <strong>R</strong>ead 
      <strong>U</strong>pdate
      <strong>D</strong>elete
      <a href="http://schema.org/">Schema.org</a> entities in 
      <a href="http://json-ld.org/">JSON-LD</a>
  </div> 
 <h2>{{ name }}</h2>
 <form action="/crud" method="POST" class="form-horizontal">
 % for form_name in sorted(form._fields):
 % sub_form = getattr(form, form_name)
 % sub_form_label = sub_form.name.replace("_", " ").title()
 <div class="control-group">
  <label class="control-label" for="{{ sub_form.name }}">{{ sub_form_label  }}</label>
  <div class="controls">
  % for field_name in sorted(sub_form._fields):
  % field = getattr(sub_form, field_name)
   {{!field(on_click='"alert('hello')"'}}
  % end
  </div>
 </div>
 % end
</form>
%rebase base
