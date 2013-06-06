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
 <ul class="nav nav-tabs" id="schema_entity_tab"
  <li class="active"><a href="#tab1" data-toggle="tab">Active</a></li>
  <li><a href="#tab2" data-toggle="tab">Tab 2</a></li>
  <li><a href="#tab3" data-toggle="tab">Final Tab</a></li>
 </ul>
 <div class="tab-content">
  <div class="tab-pane active" id="tab1">
   FORM Element 1
  </div> 
  <div class="tab-pane" id="tab2">
   FORM Element 2
  </div>
  <div class="tab-pane" id="tab3">
   <p>Form Element 3</p>
  </div>
 </div>
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
%rebase base
