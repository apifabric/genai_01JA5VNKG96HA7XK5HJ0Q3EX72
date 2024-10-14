import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'InventoryItem-new',
  templateUrl: './InventoryItem-new.component.html',
  styleUrls: ['./InventoryItem-new.component.scss']
})
export class InventoryItemNewComponent {
  @ViewChild("InventoryItemForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}