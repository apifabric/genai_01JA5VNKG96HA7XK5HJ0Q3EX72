import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './InventoryItem-card.component.html',
  styleUrls: ['./InventoryItem-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.InventoryItem-card]': 'true'
  }
})

export class InventoryItemCardComponent {


}