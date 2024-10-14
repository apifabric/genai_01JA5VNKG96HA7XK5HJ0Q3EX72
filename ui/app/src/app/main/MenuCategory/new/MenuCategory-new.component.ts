import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'MenuCategory-new',
  templateUrl: './MenuCategory-new.component.html',
  styleUrls: ['./MenuCategory-new.component.scss']
})
export class MenuCategoryNewComponent {
  @ViewChild("MenuCategoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}