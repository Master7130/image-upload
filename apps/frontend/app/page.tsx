'use client';

import { ChangeEvent, useState, useRef, useEffect } from 'react';

interface FileUploadResponse {
  success: boolean;
  url: string;
}

export default async function Index() {
  const [error, setError] = useState('');

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = async () => {
    const inputElement = fileInputRef.current;
    if (!inputElement || !inputElement.files) {
      setError('Please upload an image!');
      return;
    }

    const file = inputElement.files[0];

    const formData = new FormData();
    if (file) formData.append('file', file);

    try {
      const res = await fetch(`${process.env.SERVER}/image`, {
        method: 'POST',
        body: formData,
      });

      const data: FileUploadResponse = await res.json();

      if (data.success) {
        console.log('Image uploaded to:', data.url);
      } else {
        throw new Error('Upload failed');
      }
    } catch (error) {
      console.error(error);
      setError("Error: "  + error)
    }
  };

  return (
    <div className="flex flex-col gap-y-6 items-center">
      <span>{error}</span>
      <input
        type="file"
        className="block w-fit text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        ref={fileInputRef}
      />
      <input
        type="submit"
        className="block w-fit px-10 py-2 rounded-md text-blue-700 bg-blue-50 hover:bg-blue-100"
        onClick={handleSubmit}
      />
      <div>Image URL: </div>
    </div>
  );
}
