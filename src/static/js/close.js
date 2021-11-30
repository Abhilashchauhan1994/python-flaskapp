document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete .modal') || []).forEach(($delete) => {
      const $notification = $delete.parentNode;
  
      $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification);
      });
    });
  });