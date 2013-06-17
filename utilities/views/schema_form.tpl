<div class="container">
 <div><strong>C</strong>reate 
      <strong>R</strong>ead 
      <strong>U</strong>pdate
      <strong>D</strong>elete
      <a href="http://schema.org/">Schema.org</a> entities in 
      <a href="http://json-ld.org/">JSON-LD</a>
  </div> 
 <h2>{{ name }}</h2>

<ul class="nav nav-tabs" id="myTab">
  <li class="active"><a href="#home">Home</a></li>
  <li><a href="#profile">Profile</a></li>
  <li><a href="#messages">Messages</a></li>
  <li><a href="#settings">Settings</a></li>
</ul>
 
<div class="tab-content">
  <div class="tab-pane active" id="home">...</div>
  <div class="tab-pane" id="profile">...</div>
  <div class="tab-pane" id="messages">...</div>
  <div class="tab-pane" id="settings">...</div>
</div>
 

 <form action="/crud" method="POST" class="form-horizontal">
 <input type="submit" class="btn btn-primary"></input>
 % for form_name in sorted(form._fields):
 % sub_form = getattr(form, form_name)
 % sub_form_label = sub_form.name.replace("_", " ").title()
 <div class="control-group">
  <label class="control-label" for="{{ sub_form.name }}">{{ sub_form_label  }}</label>
  <div class="controls">
  % for field_name in sorted(sub_form._fields):
  % field = getattr(sub_form, field_name)
   {{!field}}
  % end
  </div>
 </div>
 % end
</form>
<script>
  $(function () {
    $('# a:last').tab('show');
  })
</script>


%rebase base
